class Add(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return (self.a + self.b)


if __name__ == '__main__':
    add_obj = Add(5,10)
    print(add_obj.addition())

