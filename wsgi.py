# -*- coding: utf-8 -*-
"""Wsgi script.

Usage:
FLASK_APP=./wsgi.py flask run"""

import sys
import os
import unittest
import tests.tests as tests
import coverage


project = "fbone"  #pylint: disable=invalid-name

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
from fbone import create_app #pylint: disable=wrong-import-position
virtualenv()
application = create_app()   #pylint: disable=invalid-name
#application = flask.Flask(__name__)

@application.cli.command()
def setdir():
    """Create a default db"""
    from fbone.utils import INSTANCE_FOLDER_PATH
    if os.path.isdir(INSTANCE_FOLDER_PATH):
        pass
    else:
        os.makedirs(INSTANCE_FOLDER_PATH)

@application.cli.command()
def cov():
    """Runs the unit tests with coverage."""
    print 'Please run the script ./get_coverage.py'

@application.cli.command()
def test():
    """Runs the unit tests."""
    print 'please run python -m unittest discover'
    # http://stackoverflow.com/questions/14282783/call-a-python-unittest-from-another-script-and-export-all-the-error-messages
    #from StringIO import StringIO
    #stream = StringIO()
    #runner = unittest.TextTestRunner(stream=stream)
    #result = runner.run(unittest.makeSuite(tests.TestFrontend))
    #print result
    #print result.testsRun
    #print result.errors
    #print result.failures
    #print 'end'
