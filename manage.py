"""Utility for manageing tests and coverage"""
import unittest
import coverage
from wsgi import application
from tests import TestFrontend

COV = coverage.coverage(branch=True,
                        include='fbone/*',
                        omit=['*/__init__.py', '*/config/*'])
COV.start()

app = application() #pylint: disable=invalid-name

@app.cli.command()
def cov():
    """Runs the unit tests with coverage."""
    print 'run coverage'
    tests = unittest.TestSuite()
    tests.addTest(TestFrontend())
    unittest.TextTestRunner().run(tests)
    COV.stop()
    print 'Coverage Summary:'
    COV.report()
