from testcase import TestCase, WasRun, TestResult, TestSuite


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        result = TestResult()
        test.run(result)
        assert(test.log == 'setUp testMethod tearDown ')

    def testResult(self):
        test = WasRun('testMethod')
        result = TestResult()
        test.run(result)
        assert(result.summary() == '1 run, 0 failed')

    def testFailedResult(self):
        test = WasRun('testBrokenMethod')
        result = TestResult()
        test.run(result)
        assert(result.summary() == '1 run, 1 failed')

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert(result.summary() == '1 run, 1 failed')

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        result = TestResult()
        suite.run(result)
        assert(result.summary() == '2 run, 1 failed')


suite = TestSuite()
suite.add(TestCaseTest('testTemplateMethod'))
suite.add(TestCaseTest('testResult'))
suite.add(TestCaseTest('testFailedResult'))
suite.add(TestCaseTest('testFailedResultFormatting'))
suite.add(TestCaseTest('testSuite'))

result = TestResult()
suite.run(result)

print(result.summary())