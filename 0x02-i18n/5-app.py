#!/usr/bin/env python3

"""
Mock Logging
"""
from flask import Flask, render_template, g, request
app = Flask(__name__)

# User table
USERS = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Define get_user function


def get_user(user_id):
    """get user"""
    return USERS.get(user_id)

# Define before_request function


@app.before_request
def before_request():
    login_as = request.args.get('login_as')
    if login_as:
        g.user = get_user(int(login_as))
    else:
        g.user = None

# Define route


@app.route('/')
def index():
    """index"""
    welcome_message = ""
    if g.user:
        welcome_message = f"You are logged in as {g.user['name']}."
    else:
        welcome_message = "You are not logged in."
    return render_template('index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
