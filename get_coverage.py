# -*- coding: utf-8 -*-
"""Runs the unit tests with coverage.

Usage:
python ./get_coverage.py"""
# pylint: disable=invalid-name

from StringIO import StringIO
import sys
import os
import unittest
import coverage

TEST_DIR = 'tests'

def virtualenv():
    """Activate the virtualenv"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    activate_this = os.path.join(dir_path, 'venv', "bin/activate_this.py")
    execfile(activate_this, dict(__file__=activate_this))

class Tests(object): #pylint: disable=no-init,too-few-public-methods
    """Class finding all available tests"""
    def suite(self): #pylint: disable=no-self-use
        """Function stores all the modules to be tested"""
        modules_to_test = []
        test_dir = os.listdir(TEST_DIR)
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))

        alltests = unittest.TestSuite()
        for module in map(__import__, modules_to_test): #pylint: disable=bad-builtin
            #module.testvars = ["variables you want to pass through"]
            #module.testvars = []
            alltests.addTest(unittest.findTestCases(module))
        return alltests

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
TEST_DIR_PATH = os.path.join(BASE_DIR, TEST_DIR)
sys.path.append(TEST_DIR_PATH)

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
