from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "git@github.com:Leo-Song/djangotest.git"
env.user = 'root'
env.password = 'Net263#cn'
env.hosts = ['leoblog.com']
env.port = '22'

def deploy():
    source_folder = '/root/py36env/workspace/LeoBlog'

    run('cd %s && git pull' %source_folder)
    run ("""
    cd {} &&
    /root/py36env/bin/pip install -r requirements.txt &&
    /root/py36env/bin/python manage.py collectstatic --noinput &&
    /root/py36env/bin/python manage.py migrate
    """.format(source_folder))
    sudo('systemctl restart gunicorn-leoblog.service')
    sudo('/opt/nginx/sbin/nginx -s reload')