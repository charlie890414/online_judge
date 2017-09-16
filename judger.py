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
    submission.objects.filter(id=judging.id).update(status='judging')
    name = 'judger'+str(judging.id)  
    problem = os.path.join(os.getcwd(), os.path.dirname(str(judging.problem.ans).replace('/','\\')))
    code = os.path.join(os.getcwd(), os.path.dirname(str(judging.code).replace('/','\\'))) 
    to1 = "/tmp/problem"
    to2 = "/tmp/code"
    if judging.problem.test=="":
        if judging.lang == "python3":
            bash = "\"python3 tmp/code/*.py > tmp/code/out.txt\""
    else:
        if judging.lang == "python3":
            bash = "\"python3 tmp/code/*.py < tmp/problem/in.txt > tmp/code/out.txt\""
    cmd = 'docker run -dit -v %s:%s -v %s:%s --memory="65536" --memory-swap="65536" --cpu-quota=75000 --name %s aefb65fc0d2e bash -c %s' % (problem,to1,code,to2,name,bash)
    tmp = subprocess.Popen(cmd)
    for i in range(2):        
        time.sleep(1)
        if tmp.poll()!=None:
            break
        elif  i == 10:
            tmp.terminate()
            submission.objects.filter(id=judging.id).update(state='TLE')
    cmd = 'docker rm %s' %(name)
    tmp = subprocess.call(cmd)
    ans =open(problem+"\\ans.txt").read()
    out =open(code+"\\out.txt").read()
    print(ans)
    print(out)
    try:
        if ans == out:
            submission.objects.filter(id=judging.id).update(status='AC')
        else: 
            submission.objects.filter(id=judging.id).update(status='WA or Error')
    except:
        submission.objects.filter(id=judging.id).update(status='Error')
    finally:
        return
if __name__ == '__main__':
    while True:
        judging=submission.objects.filter(status='waiting')
        if judging:
            for mission in judging:
                while threading.active_count() > 10:
                    time.sleep(1)
                the_thread =  threading.Thread(target=rundocker(mission))
                the_thread.start()            