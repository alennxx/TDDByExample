from unittest import TestCase


from WasRun import WasRun

class TestCaseTest(TestCase):

    def testRunning(self):
        test = WasRun("testMethod")
        assert (test.wasRun)
        test.run()
        assert (test.wasRun)

