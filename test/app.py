class Animal(object):
    pass

class Dog(Animal):
    def talk(self):
        return "whoof whoof"

class Cat(Animal):
    def talk(self):
        return "miao"

class Pig(Animal):
    def talk(self):
        return "oink oink"

def all_animals():
    # sub_class = Animal.__subclasses__()
    # for x in sub_class:
    #     print(x.talk('haha'))
    # print(sub_class)
    return Animal.__subclasses__()

if __name__ == "__main__":
    for animal in all_animals():
        print("%s says: %s" % (animal.__name__, animal().talk()))