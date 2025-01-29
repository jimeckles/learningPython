class TestClass:
    def __eq__(self, other):
        return True
a = TestClass()
print(a==1 and a==2 and a==3)
