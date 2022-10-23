from TestCaseTest import TestCaseTest
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)

#x = TestCaseTest("testRunning")
#x.run()

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())
