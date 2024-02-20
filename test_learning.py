import unittest
from help import Help


class TestLearning(unittest.TestCase):

    def test_str_reverse(self):
        print("test_str_reverse")
        forward = "this is a big program"
        reversed = "margorp gib a si siht"
        # use slice
        myReversed = forward[::-1]
        self.assertEqual(reversed, myReversed)

    def test_char_count(self):
        print("test_char_count")
        self.assertEqual("1234abcdA".lower().count("a"), 2)

    def test_or(self):
        print("test_or")
        self.assertEqual(1 or 0, True)

    def test_and(self):
        print("test_and")
        self.assertEqual(-1 and 1, True)

    def test_not_and(self):
        print("test_not_and")
        self.assertEqual(-1 and 1, not False)

    def test_len_num(self):
        print("test_len_num")
        self.assertEqual(len(["1"]), 1)

    def test_functions(self):
        print("test_functions")

        def hello(name):
            print("Hello %s" % name)
            return "Hello " + name

        self.assertEqual(hello("bob"), "Hello bob")

    def test_classes(self):
        print("test_classes")
        testVal = "var"

        class TestClass:

            def __init__(self, classVar):
                self.classVar = classVar

            def printMyStuff(self):
                return self.classVar

        myInstance = TestClass(testVal)
        self.assertEqual(myInstance.printMyStuff(), testVal)
        self.assertEqual(myInstance.classVar, testVal)

    def test_dict(self):
        myDict = {"ilooklikejson": True, "anotherone": False}
        for name, value in myDict.items():
            print("destructuring %s %s" % (name, value))
        del myDict["ilooklikejson"]
        myDict.pop("anotherone")
        print(myDict)

    def test_help(self):
        # myHelper = Help()
        myname = 'maxhelper'
        # classmethod obj factory
        myHelper = Help.makeHelper(myname)
        moduleName = "re"
        functions = myHelper.manual(moduleName)
        matches = []
        for name in functions:
            if name.find("a") >= 0:
                matches.append(name)
        matches.sort()
        # for match in matches:
        #     print("contains %s: %s\n" % ("find", match))
        #     print(help(moduleName + "." + match))
        self.assertEqual(myname, myHelper.name)


if __name__ == "__main__":
    unittest.main()
