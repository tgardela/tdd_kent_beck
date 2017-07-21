class TestCase():
    def __init__(self, name):
        self.name = name


    # takes attributes: self and self.name and calls a method that has a name == self.name
    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)


    def testMethod(self):
        self.wasRun = 1

