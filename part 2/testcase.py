class TestCase():
    def __init__(self, name):
        self.name = name


    def setUp(self):
        pass


    # takes attributes: self and self.name and calls a method that has a name == self.name
    def run(self):
        # result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()


    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)


    def setUp(self):
        self.log = 'setUp '


    def testMethod(self):
        self.log += 'testMethod '


    def tearDown(self):
        self.log += 'tearDown '



class TestResult():
    def summary(self):
        return '1 run, 0 failed'