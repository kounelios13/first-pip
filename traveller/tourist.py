class Tourist():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("{} says hello.".format(self.name))

    def say_magic_number(self, number):
        print("{} says number {}".format(self.name, number * 2))
