class Help:

    def __init__(self, name) -> None:
        self.name = name

    def manual(self, moduleName):
        print("manual instance method %s" % self)
        self.__class__.logAccess()
        listOfNames = dir(moduleName)
        listOfNames.sort()
        # for name in listOfNames:
        #     print("%s %s" % (moduleName, name))
        return listOfNames

    @classmethod
    def logAccess(cls):
        print("logAccess classmethod")
        print(cls)
        return "class method called", cls

    @classmethod
    def makeHelper(cls, name):
        return cls(name)
