class myclass:

    __privateVar = 27

    def __privMeth(self):
        print("im inside class myclass")

    def hello(self):
        print("private var value: ",myclass.__privateVar)

foo = myclass()
foo.hello()
foo.__privMeth()        