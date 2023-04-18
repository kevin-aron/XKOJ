from __future__ import absolute_import
from celery import shared_task
import os
import subprocess
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.judge import compiles

@shared_task(name = "evaluate_submission")
def evaluate_submission(sub_id):
    try:
        submission = Submission.objects.get(pk = sub_id)
    except:
        print("Submission with id = {} not found".format(sub_id))
        return 
    username = submission.submitter.user.username
    cur_problem = submission.problem
    print(cur_problem)
    cur_problem.num_submissions += 1
    tl = cur_problem.time_limit
    timeout_lst = ["timeout",str(tl)]
    ##
    tc = TestCase.objects.get(problem = cur_problem)
    input_filename = tc.input_file.name
    output_filename = tc.output_file.name
    langu = submission.lang
    filename = ''
    compiler = ''
    filemir = "{}_{}".format(username,sub_id)
    executable = "{}_{}.out".format(username,sub_id)
    if langu == 'C':
        langu = 'gcc'
        filename = "{}_{}.c".format(username,sub_id)
    elif langu == 'CPP':
        langu = 'g++'
        filename = "{}_{}.cpp".format(username,sub_id)
    elif langu == 'JAVA':
        langu = 'javac'
        filename = "{}_{}.java".format(username,sub_id)
    elif langu == 'PYTH':
        langu = 'python2'
        filename = "{}_{}.py".format(username,sub_id)
    elif langu == 'PYTH3':
        langu = 'python3'
        filename = "{}_{}.py".format(username,sub_id)

    user_code = open("submissions/{}".format(filename),"w+")
    print(submission.code,file = user_code)
    user_code.close()
    if langu == 'gcc':
        build = "{} submissions/{} -o process/{} -Wall -lm -O2 --static -DONLINE_JUDGE".format(langu,filename,executable)
    elif langu == 'g++':
        build = "{} submissions/{} -O2 -Wall -lm --static -DONLINE_JUDGE -o process/{}".format(langu,filename,executable)
    elif langu == 'javac':
        build = "{} submissions/{}".format(langu,filename)
    elif langu == 'python2':
        build = "{} -m py_compile submission/{}".format(langu,filename)
    elif langu == 'python3':
        build = "{} -m py_compile submission/{}".format(langu,filename)
    p = subprocess.Popen(build,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = p.communicate()
    if p.returncode == 0:
        user_output_filename = "testcases/ans/{}_{}.output".format(username,sub_id)
        optional_lst = ["python3","run.py","process/{}".format(executable),input_filename,user_output_filename,str(tl)]
        run_code = subprocess.check_output(optional_lst,shell = False)
        run_code = int(run_code.decode("utf-8"))
        #code_ans = open("{}".format(user_output_filename))
        if run_code == 124:
            print("time limit execeeded")
            submission.status = "TL"
            submission.save()
            cur_problem.num_tle+=1
            cur_problem.save()
        elif run_code != 0:
            print("run time error")
            submission.status = "RE"
            submission.save()
            cur_problem.num_re+=1
            cur_problem.save()
        else:
            differ = subprocess.call(["diff","{}".format(user_output_filename),output_filename])
            if differ == 0:
                print("AC")
                submission.status = "AC"
                submission.save()
                cur_problem.num_ac+=1
                cur_problem.save()
            else:
                print("WA")
                submission.status = "WA"
                submission.save()
                cur_problem.num_wa+=1
                cur_problem.save()
    else:
        submission.status = "CE"
        cur_problem.num_ce += 1
        cur_problem.save()
        submission.save()
        os.remove("submissions/{} process/{}".format(filename,filemir))

    

    subprocess.Popen('rm submissions/{} process/{}.out {}'.format(filename,filemir,user_output_filename),shell=True)
    return 'eva_now'