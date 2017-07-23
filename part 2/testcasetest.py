from testcase import TestCase, WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')


    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert(test.log == 'setUp testMethod tearDown ')


    def testResult(self):
        test = WasRun('testMethod')
        result = test.run()
        assert(result.summary() == '1 run, 0 failed')


TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()

