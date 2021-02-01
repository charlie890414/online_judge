import os
import time
import django
#-*- coding:utf-8 -*-
os.environ['DJANGO_SETTINGS_MODULE'] ='online_judge.settings'
django.setup()

from judge.models import *

import docker
client = docker.from_env()


def rundocker(judging):
    # submission.objects.filter(id=judging.id).update(status='judging')
    name = 'judger'+str(judging.id)
    print(name)
    problem = os.path.join(os.getcwd(), os.path.dirname(
        str(judging.problem.ans).replace('/', '\\')))
    code = os.path.join(os.getcwd(), os.path.dirname(
        str(judging.code).replace('/', '\\')))
    to1 = "/tmp/problem"
    to2 = "/tmp/code"

    try:
        time.sleep(1)
        client.containers.run("judger:latest", volumes={
            problem: {'bind': to1, 'mode': 'ro'},
            code: {'bind': to2, 'mode': 'rw'}
        }, environment=[
            f"lang={judging.lang}"
        ], network_disabled=True, auto_remove=True)

        ans = open(problem+"\\ans.txt", 'rb').read()
        stdout = open(code+"\\out.txt", 'rb').read()
        stderr = open(code+"\\err.txt", 'rb').read()
        res = open(code+"\\res.txt", 'rb').read().strip()

        print(ans, stdout, stderr, res)

        if res == b"124":
            submission.objects.filter(id=judging.id).update(status='TLE')
            return

        if res == b"0" and ans == stdout:
            submission.objects.filter(id=judging.id).update(status='AC')
            if str(judging.problem.id) not in set(judging.member.AC_problem.split()):
                member.objects.filter(id=judging.member.id).update(
                    AC_problem=judging.member.AC_problem+' '+str(judging.problem.id)+' ')
                member.objects.filter(id=judging.member.id).update(
                    AC=judging.member.AC+1)
                if judging.id > judging.member.update:
                    member.objects.filter(
                        id=judging.member.id).update(update=judging.id)
        else:
            submission.objects.filter(id=judging.id).update(status='WA')
    except Exception as e:
        print(e)
        submission.objects.filter(id=judging.id).update(status='Error')


if __name__ == '__main__':
    while True:
        judging = submission.objects.filter(
            status='waiting').order_by('id').reverse()
        if judging:
            for mission in judging:
                rundocker(mission)
