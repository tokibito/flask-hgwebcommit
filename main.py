# app
from hgwebcommit import app

# config
SECRET_KEY = '(secret key)'
HGWEBCOMMIT_REPOSITORY = '/path/to/repository'
HGWEBCOMMIT_ENCODING = 'utf-8'

# actions
HGWEBCOMMIT_ACTIONS = (
    # 'hgwebcommit.actions.hello',
)

if __name__ == '__main__':
    app.debug = True
    app.config.from_object(__name__)
    app.run(host='0.0.0.0')
