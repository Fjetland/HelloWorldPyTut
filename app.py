class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Woof")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog = Dog()
dog.walk()
dog.bark()
