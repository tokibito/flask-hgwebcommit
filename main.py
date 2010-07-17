# app
from hgwebcommit import app

# config
SECRET_KEY = '(secret key)'
HGWEBCOMMIT_REPOSITORY = '/home/tokibito/_work/repos'
HGWEBCOMMIT_ENCODING = 'utf-8'

if __name__ == '__main__':
    app.debug = True
    app.config.from_object(__name__)
    app.run(host='0.0.0.0')
