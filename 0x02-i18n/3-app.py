#!/usr/bin/env python3
'''Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    '''Configure languages available for app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''Determines best mach with supported languages'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    ''' Returns index template'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
