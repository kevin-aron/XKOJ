import os
import subprocess
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission

def compiles(sub_id,langu,username,submission):
    build_cmd = {
        "gcc"     :"gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "g++"     :"g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java"    :"javac Main.java",
        "python2" :"python2 -m py_compile main.py",
        "python3" :"python3 -m py_compile main.py",
    }
    dir_work = ''
    if langu == "gcc":
        dir_work = "{}_{}.c".format(username,sub_id)
    elif langu == "g++":
        dir_work = "{}_{}.cpp".format(username,sub_id)
    user_code = open("submissions/{}".format(dir_work),"w+")
    print(submission.code,file = user_code)
    user_code.close()
    p = subprocess.Popen(build_cmd[langu],shell=True,cwd="~/xkoj/submissions/{}".format(dir_work),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(p)
    out,err = p.communicate()
    if p.returncode == 0:
        return True
    update_compile_info(sub_id,err+out)
    return False