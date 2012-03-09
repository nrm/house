from fabric.api import *
from os.path import join

env.hosts = ['example.com']

PROJECT_NAME = 'house_shop'
PROJECT_DIR = join('/home/bezrukov/Envs/%s'%PROJECT_NAME, 'source')


def run_in_virtualenv(command):
    run('source %s/../bin/activate && %s' %
        (PROJECT_DIR, command))

def commit_to_hub():
    message = raw_input("Enter a git commit message:  ")
    local("git add . && git commit -m \"%s\"" % message)
    local("git push origin master")

def deploy():
    with cd(PROJECT_DIR):
        run('git pull')
        run_in_virtualenv('pip install -r requirements.txt')
        run_in_virtualenv('python manage.py syncdb')
        run_in_virtualenv('python manage.py migrate')
        #run_in_virtualenv('./manage.py clear_cache')
        run('sudo supervisorctl -c /etc/supervisor/supervisord.conf restart %s'%PROJECT_NAME)
        run('sudo supervisorctl -c /etc/supervisor/supervisord.conf status %s'%PROJECT_NAME)
        #run('restart ' + PROJECT_NAME)


#import settings
#db_settings = settings.DATABASES['default']
#
#
#def fetch_db():
#    with cd(PROJECT_DIR):
#        run('mysqldump %(NAME)s -u %(BACKUP_USER)s -p%(BACKUP_PASSWORD)s '
#            '--skip-lock-tables > dump.sql' % db_settings)
#        get('dump.sql', 'dump.sql')
#    local('./manage.py flush --noinput')
#    local('./manage.py dbshell < dump.sql')
