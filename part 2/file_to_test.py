class WasRun:
    def __init__(self, name):
        self.wasRun = None
        self.name = name


    def testMethod(self):
        self.wasRun = 1

    #this method takes attributes: self and self.name, and calls a method that has a name == self.name
    def run(self):
        method = getattr(self, self.name)
        method()