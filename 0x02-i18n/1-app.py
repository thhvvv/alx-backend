#!/usr/bin/env python3
'''Then instantiate the Babel object in your app. Store it in a module-level variable named babel.'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Configure languages available for app; default=en and UTC'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    ''' Returns index template'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
