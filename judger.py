import os
import sys
import time
import django

os.environ['DJANGO_SETTINGS_MODULE'] ='online_judge.settings'
from online_judge import settings
django.setup()

from judge.models import *
import subprocess
import filecmp
def rundocker(judging):    
    problem = os.path.join(os.getcwd(), os.path.dirname(str(judging.problem.ans).replace('/','\\')))
    code = os.path.join(os.getcwd(), os.path.dirname(str(judging.code).replace('/','\\')))        
    to1 = "/tmp/problem"
    to2 = "/tmp/code"
    if judging.problem.test=="": 
        bash = "\"python3 tmp/code/*.py &> tmp/code/out.txt\""
    else:
        bash = "\"python3 tmp/code/*.py< tmp/problem/in.txt &> tmp/code/out.txt\""
    cmd = 'docker run -dit -v %s:%s -v %s:%s --memory="32M" --memory-swap="32M" --cpu-quota=75000 --name judge aefb65fc0d2e bash -c %s' % (problem,to1,code,to2,bash)
    tmp = subprocess.Popen(cmd)
    # cmd = 'docker start judge'
    # tmp = subprocess.call(cmd)
    # cmd = 'docker exec -it judge bash'
    # tmp = subprocess.Popen(cmd)
    time.sleep(10)
    if tmp.poll():
        tmp.terminate()
        submission.objects.filter(id=judging.id).update(state='TLE')
    cmd = 'docker stop judge'
    tmp = subprocess.call(cmd)
    cmd = 'docker rm judge'
    tmp = subprocess.call(cmd)
    ans =problem+"\\ans.txt"
    out =code+"\\out.txt"
    try:
        if filecmp.cmp(ans,out):
            submission.objects.filter(id=judging.id).update(state='AC')
        else:
            submission.objects.filter(id=judging.id).update(state='WA or Error')
    except:
        submission.objects.filter(id=judging.id).update(state='Error')
    finally:
        return
judging=list(submission.objects.filter(state='waiting'))
if judging:
    for mission in judging:
        rundocker(mission)