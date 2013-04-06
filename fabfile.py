from __future__ import with_statement
from fabric.api import env
from fabric.api import run,sudo, local, settings, abort, cd, prefix
from fabric.contrib.project import upload_project
from fabric.contrib.files import exists
from fabric.operations import put
from fabric.contrib.console import confirm
from fabric.contrib import django

env.hosts = ['deploy@teaching.shmooph.com']
code_dir = '/home/deploy/teaching.shmooph.com'
APPS_UNDER_TEST = ['worksheets', ]

def test():
    django.settings_module('teaching.settings_test')
    for app in APPS_UNDER_TEST:
        local('teaching/manage.py harvest -a %s' % app)

def create_environment():
    sudo('apt-get install libjpeg-dev libjpeg-turbo8 libjpeg-turbo8-dev '
         'zlib1g-dev libfreetype6 libfreetype6-dev libyaml-dev '
         'python-dev python-virtualenv postgresql-server-dev-all libpq-dev')
    run('mkdir -p %s' % code_dir)
    put('requirements.txt', code_dir)
    with cd(code_dir):
        run('virtualenv --distribute --no-site-packages .')
        run('source bin/activate; pip install -r requirements.txt')
        run('mkdir -p static')
        run('mkdir -p media')

def copy_project():
    """
    """
    local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
    with cd(code_dir):
        put('templates', code_dir)
        put('teaching', code_dir)
        run("find . -name '*.pyc' -print0|xargs -0 rm")


def init_project():
    """
    Initialize Django and the database
    """
    with cd(code_dir):
        with prefix('source bin/activate'):
            run('DJANGO_SETTINGS_MODULE=teaching.settings_deploy python teaching/manage.py syncdb')
            run('DJANGO_SETTINGS_MODULE=teaching.settings_deploy python teaching/manage.py migrate')
            run('DJANGO_SETTINGS_MODULE=teaching.settings_deploy python teaching/manage.py collectstatic --noinput')


def restart():
    sudo("service teaching.shmooph.com restart")
    sudo("/etc/init.d/nginx restart")


def deploy():
    create_environment()
    copy_project()
    init_project()
    restart()
