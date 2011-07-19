# app
from hgwebcommit import app

# config
SECRET_KEY = '(secret key)'
HGWEBCOMMIT_REPOSITORY = '/path/to/repository'
#HGWEBCOMMIT_REPOSITORY_BACKEND = 'hgwebcommit.repository.dummy.DummyRepository'
HGWEBCOMMIT_ENCODING = 'utf-8'
HGWEBCOMMIT_ALLOW_COMMIT = True

# actions
HGWEBCOMMIT_ACTIONS = (
    #'hgwebcommit.actions.hello',
)

# command actions
#from hgwebcommit.actions import ExecuteCommandAction, manager
#act = ExecuteCommandAction('echo_command', 'echo command', ['echo', 'hello'])
#manager.add(act)

# logging
#import logging
#from hgwebcommit.logger import MonthlyRotatingFileHandler
#logging_handler = MonthlyRotatingFileHandler('/var/log/webcommit.log')
#logging_handler.setLevel(logging.INFO)
#logging_handler.suffix = '%Y%m'
#logging_handler.setFormatter(logging.Formatter(
#    '%(asctime)s %(message)s',
#    '%Y-%m-%d %H:%M:%S'
#))
#app.logger.addHandler(logging_handler)

if __name__ == '__main__':
    app.debug = True
    app.config.from_object(__name__)
    app.run(host='127.0.0.1')
