import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/WeighTrack')  #You must add your project here or 500
#Switch to new python
#You may try to replace $HOME with your actual path
if sys.version < "2.7.5": os.execl("/home/burkugler/weighty/env/bin/python", "python2.7", *sys.argv)

sys.path.insert(0,'/home/burkugler/weighty/env/bin')

# sys.path.insert(0,'/home/burkugler/weighty/env/lib/python2.7/site-packages/django')
sys.path.insert(0,'/home/burkugler/weighty/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "WeighTrack.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
