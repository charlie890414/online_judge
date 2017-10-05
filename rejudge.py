import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] ='online_judge.settings'
from online_judge import settings
django.setup()
from judge.models import *

if __name__ == '__main__':
    judging=submission.objects.all()
    for mission in judging:
        submission.objects.filter(id=mission.id).update(status='waiting')