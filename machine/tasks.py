from celery import shared_task
import os
import subprocess
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.models.game.game import Game
from machine.models.game.gamerk import GameRk
from machine.models.game.gamesubmission import GameSubmission


@shared_task(name = "evaluate_submission")
def evaluate_submission(sub_id):
	try:
		submission = Submission.objects.get(pk=sub_id)
	except:
		return 
	username = submission.submitter.user.username
	cur_problem = submission.problem
	cur_problem.num_submissions += 1
	tl = cur_problem.time_limit
	timeout_lst = ["timeout", str(tl)]
	langu = submission.lang
	codefile = {
		"C"    :"{}_{}.c",
		"CPP"  :"{}_{}.cpp",
		"JAVA" :"{}_{}.java",
		"PYTH3":"{}_{}.py",
	}
	codelang = {
		"C"    :"gcc",
		"CPP"  :"g++",
		"JAVA" :"javac",
		"PYTH3":"python3",
	}
	filename = ''
	compiler = ''
	filemir = "{}_{}".format(username,sub_id)
	filename = codefile[langu].format(username,sub_id)
	langu = codelang[langu];
	executable = "{}_{}".format(username,sub_id)
	user_code = open("submissions/{}".format(filename),"w+")
	print(submission.code,file = user_code)
	user_code.close()
	if langu == 'gcc':
		build = "{} submissions/{} -o process/{} -Wall -lm -O2 --static -DONLINE_JUDGE".format(langu,filename,executable)
	elif langu == 'g++':
		#build = "{} submissions/{} -O2 -Wall -lm --static -DONLINE_JUDGE -o process/{}".format(langu,filename,executable)
		build = "g++ submissions/{} -o process/{}".format(filename,executable)
	elif langu == 'javac':
		build = "{} submissions/{} -d process/".format(langu,filename)
	elif langu == 'python3':
		build = "{} -m py_compile submission/{}".format(langu,filename)
	p = subprocess.Popen(build, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	stdout, stderr = p.communicate()
	testcases = TestCase.objects.filter(problem=cur_problem)
	cnt = 1
	allstate = []
	for tc in testcases:
		input_filename = tc.input_file.name
		output_filename = tc.output_file.name
		user_output_filename = "testcases/ans/{}_{}_{}.out".format(username,sub_id,cnt)
		cnt = cnt + 1
		if p.returncode == 0:
			optional_lst = ["python3","run.py","process/{}".format(executable),input_filename,user_output_filename,str(tl)]
			run_code = subprocess.check_output(optional_lst,shell = False)
			try:
			    run_code = int(run_code.decode("utf-8"))
			except ValueError:
			    run_code = 0
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
			allstate.append("CE")

	ac_num = 0
	flag = 1
	submission.idcode = "{}_{}".format(username,sub_id)
	submission.link = "http://8.130.110.219:8000/content/submission/{}_{}".format(username,sub_id)
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

	return "evaluate_submission"

@shared_task(name = "game_submission")
def game_submission(gid, gsub_id, submission_data):
	try:
		gamesubmission = GameSubmission.objects.get(id=int(gsub_id))
	except:
		return 
	langu = gamesubmission.lang
	gamesubmission.link="http://8.130.110.219:8000/content/submission/{}".format(gamesubmission.idnum)
	sub_id = gamesubmission.idnum
	game = Game.objects.get(code=gid)
	username = gamesubmission.submitter.user.username
	cur_problem = gamesubmission.problem
	cur_problem.num_submissions += 1
	tl = cur_problem.time_limit
	timeout_lst = ["timeout", str(tl)]
	codefile = {
		"C"    :"{}_{}.c",
		"CPP"  :"{}_{}.cpp",
		"JAVA" :"{}_{}.java",
		"PYTH3":"{}_{}.py",
	}
	codelang = {
		"C"    :"gcc",
		"CPP"  :"g++",
		"JAVA" :"javac",
		"PYTH3":"python3",
	}
	filename = ''
	compiler = ''
	filemir = "{}_{}".format(username,sub_id)
	filename = codefile[langu].format(username,sub_id)
	langu = codelang[langu];
	executable = "{}_{}".format(username,sub_id)
	user_code = open("submissions/{}".format(filename),"w+")
	print(gamesubmission.code,file = user_code)
	user_code.close()
	if langu == 'gcc':
		build = "{} submissions/{} -o process/{} -Wall -lm -O2 --static -DONLINE_JUDGE".format(langu,filename,executable)
	elif langu == 'g++':
		#build = "{} submissions/{} -O2 -Wall -lm --static -DONLINE_JUDGE -o process/{}".format(langu,filename,executable)
		build = "g++ submissions/{} -o process/{}".format(filename,executable)
	elif langu == 'javac':
		build = "{} submissions/{} -d process/".format(langu,filename)
	elif langu == 'python3':
		build = "{} -m py_compile submission/{}".format(langu,filename)
	p = subprocess.Popen(build, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	stdout, stderr = p.communicate()
	testcases = TestCase.objects.filter(problem=cur_problem)
	cnt = 1
	allstate = []
	for tc in testcases:
		input_filename = tc.input_file.name
		output_filename = tc.output_file.name
		user_output_filename = "testcases/ans/{}_{}_{}.out".format(username,sub_id,cnt)
		cnt = cnt + 1
		if p.returncode == 0:
			optional_lst = ["python3","run.py","process/{}".format(executable),input_filename,user_output_filename,str(tl)]
			run_code = subprocess.check_output(optional_lst,shell = False)
			try:
			    run_code = int(run_code.decode("utf-8"))
			except ValueError:
			    run_code = 0
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
			allstate.append("CE")

	ac_num = 0
	flag = 1
	gamerk = GameRk.objects.get(game=game, player=gamesubmission.submitter)
	
	
	for state in allstate:
		if state == "CE":
			gamesubmission.result = "CE"
			cur_problem.num_ce += 1
			cur_problem.save()
			gamesubmission.save()
			flag = 0
			break
		elif state == "TL":
			gamesubmission.result = "TL"
			gamesubmission.nowtime += 20
			cur_problem.num_tle += 1
			cur_problem.save()
			gamesubmission.save()
			flag = 0
			break
		elif state == "RE":
			gamesubmission.result = "RE"
			gamesubmission.nowtime += 20
			cur_problem.num_re += 1
			cur_problem.save()
			gamesubmission.save()
			flag = 0
			break
		elif state == "WA":
			gamesubmission.result = "WA"
			gamesubmission.nowtime += 20
			gamesubmission.num_wa += 1
			cur_problem.num_wa += 1
			cur_problem.save()
			gamesubmission.save()
			flag = 0
			break
		elif state == "AC":
			ac_num += 1
			gamesubmission.ac_num = ac_num
		
		if flag == 1:
			gamesubmission.result = "AC"
			gamesubmission.nowtime += 20
			gamesubmission.num_ac += 1
			cur_problem.num_ac += 1
			game.gamenum += 1
			gamerk.totalac += 1
			cur_problem.save()
			gamesubmission.save()
			game.save()
			gamerk.save()
		else:
			gamerk.failtime += 20
			gamerk.save()

	return "game_submission"








