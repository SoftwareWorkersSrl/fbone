# -*- coding: utf-8 -*-
"""Runs the unit tests with coverage.

Usage:
FLASK_APP=./getcoverate.py"""
# pylint: disable=invalid-name

from StringIO import StringIO
import sys
import os
import unittest
import coverage

def virtualenv():
    """Activate the virtualenv"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    activate_this = os.path.join(dir_path, 'venv', "bin/activate_this.py")
    execfile(activate_this, dict(__file__=activate_this))

class Tests(object): #pylint: disable=no-init,too-few-public-methods
    """Class finding all available tests"""
    def suite(self):
        """Function stores all the modules to be tested"""
        modules_to_test = []
        test_dir = os.listdir('.')
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))
        print modules_to_test

        alltests = unittest.TestSuite()
        print map(__import__, modules_to_test)
        for module in map(__import__, modules_to_test):
            #module.testvars = ["variables you want to pass through"]
            #module.testvars = []
            alltests.addTest(unittest.findTestCases(module))
        print alltests
        return alltests

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

virtualenv()

COV = coverage.coverage(branch=True,
                        include='fbone/*',
                        omit=['*/config/*'])
COV.start()
print 'run coverage'
from fbone import create_app
application = create_app()   #pylint: disable=invalid-name
TEST = Tests()
#unittest.main(defaultTest='TEST.suite')
#import tests.tests as tests
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(TEST.suite())
#result = runner.run(unittest.makeSuite(tests.TestFrontend2))
#print result
#print result.testsRun
#print result.errors
#print result.failures
COV.stop()
COV.save()
print 'Coverage Summary:'
COV.report()
COV.html_report()
