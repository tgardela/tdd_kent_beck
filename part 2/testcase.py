class TestCase():
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    # takes attributes: self and self.name and calls a method that has a name == self.name
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

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

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return '%d run, 0 failed' % self.runCount