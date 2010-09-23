from flask import Flask, g, request
from flaskext.babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'ja', 'ja_JP'])

import hgwebcommit.views
