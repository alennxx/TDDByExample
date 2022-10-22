from cgitb import reset
from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):

    def __init__(self, name):
        super().__init__(name)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown ", "Test was not correctly run!"
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary(), "Result summary is not correct"
