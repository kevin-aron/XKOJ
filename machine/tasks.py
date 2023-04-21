from celery import shared_task
import os
# 产生子进程的模块
import subprocess
# 对应的models，声明的数据库表
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission

# 装饰器 通过name属性找到该函数并调用
@shared_task(name = "evaluate_submission")
def evaluate_submission(sub_id):
	try:
		# 读取到提交元素
		submission = Submission.objects.get(pk=sub_id)
	except:
		return 
	# 提交者
	username = submission.submitter.user.username
	# 当前题目，题目提交数+1
	cur_problem = submission.problem
	cur_problem.num_submissions += 1
	# 时间限制
	tl = cur_problem.time_limit
	timeout_lst = ["timeout", str(tl)]
	# 获取语言
	langu = submission.lang
	# 定义codefile(代码文件名)
	codefile = {
		"C"    :"{}_{}.c",
		"CPP"  :"{}_{}.cpp",
		"JAVA" :"{}_{}.java",
		"PYTH3":"{}_{}.py",
	}
	filename = ''
	compiler = ''
	filemir = "{}_{}".format(username,sub_id)
	filename = codefile[langu].format(username,sub_id)
	# 保存代码到文件
	user_code = open("submissions/{}".format(filename),"w+")
	print(submission.code,file = user_code)
	user_code.close()
	# 定义编译命令
	build_cmd = {
		"C"    :"gcc {} -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
		"CPP"  :"g++ {} -O2 -Wall -lm --static -DONLINE_JUDGE -o",
		"JAVA" :"javac {}",
		"PYTH3":"python3 -m py_compile {}",
	}
	# 开启子进程编译代码->可执行文件
	p = subprocess.Popen(build_cmd[langu].format("submissions/"+filename),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p.wait() # 等待子进程结束
	stdout, stderr = p.communicate()
	# 获取当前问题所有的测试用例
	testcases = TestCase.objects.filter(problem=cur_problem)
	# 执行测试用例
	cnt = 1
	allstate = []
	for tc in testcases:
		# 测试用力的.in文件和.out文件
		input_filename = tc.input_file.name
		output_filename = tc.output_file.name
		# 定义执行文件和用户运行后输出文件
		executable = "{}_{}_{}.out".format(username,sub_id,cnt)
		user_output_filename = "testcases/ans_{}_{}_{}.out".format(username,sub_id,cnt)
		cnt = cnt + 1
		if p.returncode != 0:
			# optional_lst是check_output执行必须的变量
			# 通过run.py执行测试用例并保存到user_output_filename
			optional_lst = ["python3","run.py","process/{}".format(executable),input_filename,user_output_filename,str(tl)]
			run_code = subprocess.check_output(optional_lst,shell = False)
			# run_code解码
			try:
			    run_code = int(run_code.decode("utf-8"))
			except ValueError:
			    run_code = 0
			# 开始判断
			if run_code == 124:
				allstate.append("TL")
			elif run_code != 0:
				allstate.append("RE")
			else:
				differ = subprocess.call(["diff","{}".format(user_output_filename),output_filename])
				if differ == 0:
					allstate.append("AC")
				else:
					allstate.append("WA")
		else:
			# 子进程执行失败 返回错误代码
			allstate.append("CE")
			os.remove("submissions/{} process/{}".format(filename,filemir))

	ac_num = 0
	flag = 1
	for state in allstate:
		if state == "CE":
			submission.status = "CE"
			cur_problem.num_ce += 1
			cur_problem.save()
			submission.save()
			flag = 0
			break
		elif state == "TL":
			submission.status = "TL"
			cur_problem.num_tle += 1
			cur_problem.save()
			submission.save()
			flag = 0
		elif state == "RE":
			submission.status = "RE"
			cur_problem.num_re += 1
			cur_problem.save()
			submission.save()
			flag = 0
		elif state == "WA":
			submission.status = "WA"
			cur_problem.num_wa += 1
			cur_problem.save()
			submission.save()
			flag = 0
		elif state == "AC":
			ac_num += 1
			submission.ac_num = ac_num
		
		if flag == 1:
			submission.status = "AC"
			cur_problem.num_ac += 1
			cur_problem.save()
			submission.save()

	return "submit succeeful"
