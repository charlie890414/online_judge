import os
import sys
import time
import django
import threading
os.environ['DJANGO_SETTINGS_MODULE'] ='online_judge.settings'
from online_judge import settings
django.setup()

from judge.models import *
import subprocess
import filecmp
import difflib
def rundocker(judging):
    #submission.objects.filter(id=judging.id).update(status='judging')
    name = 'judger'+str(judging.id)  
    problem = os.path.join(os.getcwd(), os.path.dirname(str(judging.problem.ans).replace('/','\\')))
    code = os.path.join(os.getcwd(), os.path.dirname(str(judging.code).replace('/','\\'))) 
    to1 = "/tmp/problem"
    to2 = "/tmp/code"
    if judging.problem.test=="":
        if judging.lang == "python3":
            bash = "\"> tmp/code/error.txt;timeout 10 python3 tmp/code/*.py > tmp/code/out.txt 2>>tmp/code/error.txt;echo $?>tmp/code/timeout.txt\""
        elif judging.lang == "c++":
            bash = "\"> tmp/code/error.txt;g++ tmp/code/*.cpp -o tmp/code/a.exe 2> tmp/code/error.txt;timeout 10 tmp/code/a.exe > tmp/code/out.txt 2>> tmp/code/error.txt;echo $?>tmp/code/timeout.txt\""
    else:
        if judging.lang == "python3":
            bash = "\"> tmp/code/error.txt;timeout 10 python3 tmp/code/*.py < tmp/problem/test.txt > tmp/code/out.txt 2>>tmp/code/error.txt;echo $?>tmp/code/timeout.txt\""
        elif judging.lang == "c++":
            bash = "\"> tmp/code/error.txt;g++ tmp/code/*.cpp -o tmp/code/a.exe 2> tmp/code/error.txt;timeout 10 tmp/code/a.exe < tmp/problem/test.txt > tmp/code/out.txt 2>>tmp/code/error.txt;echo $?>tmp/code/timeout.txt\""
    cmd = 'docker run -dit -v %s:%s:z -v %s:%s:z --privileged=true --memory="64M" --memory-swap="64M" --cpu-quota=75000 --name %s charlie890414/judger:latest bash -c %s' % (problem,to1,code,to2,name,bash)
    print(cmd)
    tmp = subprocess.call(cmd)
    time.sleep(3)
    timeout =open(code+"\\timeout.txt").read()
    print(timeout)
    if timeout == '124':
        submission.objects.filter(id=judging.id).update(status='TLE')
        return
    cmd = 'docker stop %s' %(name)
    tmp = subprocess.call(cmd)
    cmd = 'docker rm %s' %(name)
    tmp = subprocess.call(cmd)
    ans =open(problem+"\\ans.txt").read()
    out =open(code+"\\out.txt").read()
    error =open(code+"\\error.txt").read()
    print(ans)
    print(out)
    print(error)
    try:
        if error != '':
            submission.objects.filter(id=judging.id).update(status='Error')
        elif ans == out:
            submission.objects.filter(id=judging.id).update(status='AC')            
            if str(judging.problem.id) not in set(judging.member.AC_problem.split()):
                member.objects.filter(id=judging.member.id).update(AC_problem=judging.member.AC_problem+' '+str(judging.problem.id)+' ')
                member.objects.filter(id=judging.member.id).update(AC=judging.member.AC+1)
        else: 
            submission.objects.filter(id=judging.id).update(status='WA')
    except:
        submission.objects.filter(id=judging.id).update(status='Error')
    finally:
        return
if __name__ == '__main__':
    while True:
        judging=submission.objects.filter(status='waiting')
        if judging:
            for mission in judging:
                the_thread =  threading.Thread(target=rundocker(mission))
                the_thread.start()            