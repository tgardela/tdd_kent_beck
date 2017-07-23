class TestCase():
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    # takes attributes: self and self.name and calls a method that has a name == self.name
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = 'setUp '

    def testMethod(self):
        self.log += 'testMethod '

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log += 'tearDown '


class TestResult():
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return '%d run, %d failed' % (self.runCount, self.failureCount)


class TestSuite():
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)