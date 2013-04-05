from __future__ import with_statement
from fabric.api import env
from fabric.api import run,sudo, local, settings, abort, cd, prefix
from fabric.contrib.project import upload_project
from fabric.contrib.files import exists
from fabric.operations import put
from fabric.contrib.console import confirm
from fabric.contrib import django

env.hosts = ['deploy@dummy.instingo.de']
code_dir = '/home/deploy/dummy.instingo.de'
APPS_UNDER_TEST = ['events', ]

def test():
    django.settings_module('corporatehealth.settings_test')
    for app in APPS_UNDER_TEST:
        local('corporatehealth/manage.py harvest -a %s' % app)

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
        put('corporatehealth', code_dir)
        run("find . -name '*.pyc' -print0|xargs -0 rm")


def init_project():
    """
    Initialize Django and the database
    """
    with cd(code_dir):
        with prefix('source bin/activate'):
            run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py syncdb')
            run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py migrate')
            run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py collectstatic --noinput')
            # run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py loaddata corporatehealth/gamification/fixtures/auth.json')
            # run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py loaddata corporatehealth/gamification/fixtures/test_data.json')
            

def init_solr():
    """
    Initializes the SOLR schema from haystack and then restarts SOLR.
    """
    # Main directory for SOLR
    SOLR_HOME = '/usr/local/solr'

    # Directory that holds configuration files for SOLR
    SOLR_CONF = SOLR_HOME + '/example/solr/conf'
    if exists(SOLR_CONF):
        # Create the schema XML file and move it to SOLR's config directory
        with cd(code_dir):
            with prefix('source bin/activate'):
                run('DJANGO_SETTINGS_MODULE=corporatehealth.settings_deploy python corporatehealth/manage.py build_solr_schema -f /tmp/schema.xml')
        sudo('cp -f /tmp/schema.xml %s/schema.xml' % SOLR_CONF)

        # Tell upstart to restart the SOLR server
        sudo('service solr restart')

def restart():
    sudo("service dummy.instingo.de restart")
    sudo("/etc/init.d/nginx restart")


def deploy():
    create_environment()
    copy_project()
    init_project()
    # init_solr()
    restart()
