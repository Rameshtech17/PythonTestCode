class Duck(object):

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def Swim(self):
        print("Come on it, the Water's lovely")

    def quack(self):
        print("quack quack")


class Penquin(object):

    def walk(self):
        print("Waddle, Waddle, I Waddle too")

    def Swim(self):
        print("Come on it, but it's a bit chilly this South")

    def quack(self):
        print("Aer you 'avin' a larf? I'm a penguin")


def test_duck(duck):
    duck.walk()
    duck.Swim()
    duck.quack()


if __name__ == '__main__':
    # donald = Duck()
    # test_duck(donald)

    percy = Penquin()
    test_duck(percy)
