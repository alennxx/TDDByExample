from cgitb import reset
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun

class TestCaseTest(TestCase):

    def __init__(self, name):
        super().__init__(name)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(TestResult())
        assert test.log == "setUp testMethod tearDown ", "Test was not correctly run!"
    
    def testResult(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert "1 run, 0 failed" == result.summary(), "Result summary is not correct"
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert "1 run, 1 failed", result.summary
    
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary(), "Failed result summary is not correct"
    
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary(), "Test suite summary is not correct"
