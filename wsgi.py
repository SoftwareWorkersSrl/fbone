# -*- coding: utf-8 -*-
"""Wsgi script.

Usage:
FLASK_APP=./wsgi.py flask run"""

import sys, os

project = "fbone"

# Use instance folder, instead of env variables.
# specify dev/production config
#os.environ['%s_APP_CONFIG' % project.upper()] = ''
# http://code.google.com/p/modwsgi/wiki/ApplicationIssues#User_HOME_Environment_Variable
#os.environ['HOME'] = pwd.getpwuid(os.getuid()).pw_dir

# activate virtualenv
def virtualenv():
    """Activate the virtualenv"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    activate_this = os.path.join(dir_path, 'venv', "bin/activate_this.py")
    execfile(activate_this, dict(__file__=activate_this))

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# give wsgi the "application"
from fbone import create_app
virtualenv()
application = create_app()
