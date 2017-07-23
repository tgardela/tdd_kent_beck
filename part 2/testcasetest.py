from testcase import TestCase, WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')


    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert(test.log == 'setUp testMethod ')

TestCaseTest('testTemplateMethod').run()

