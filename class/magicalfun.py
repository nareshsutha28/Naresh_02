class Hello:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        print("Init method called.")


    def __str__(self):
        print("str method called.")
        print("({0}, {1})".format(self.x, self.y))
        return "Hello"

    def __add__(self, good):
        print("add method called.")
        x=self.x+good.x
        y=self.y+good.y
        return Hello(x, y)


h1=Hello(4, 8)
h2=Hello(4, 8)          

print(h1+h2)