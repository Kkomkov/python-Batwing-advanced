from re import A


class Animal:
    def eat():
        pass

    def sleep():
        pass

class Worm(Animal):
    def poop():
        pass

class Dog(Animal):
    def run():
        pass

class Cat(Animal):
    def scratch(): 
        pass

class Bird(Animal):
    def fly():
        pass

    def stuck_in_mouth():
        pass

class Tree():
    def grow_up():
        pass

worm = Worm()
cat =Cat()
dog = Dog()
bird= Bird()
tree = Tree()

class Horce(Animal):
    def run_on_4_legs():
        pass
    def kick_with__2_legs():
        pass

class Human(Animal):
    def study():  pass

    def work():
        print("doing hard job")

class Centaur(Human,Horce):
    def shoot_on_run():
        pass


creature = Centaur()
creature.kick_with__2_legs
creature.shoot_on_run
creature.kick_with__2_legs
creature.work

for animal in (worm,cat,dog,bird,tree,creature):
    print(animal.__class__.__name__, "Is animal subclass :",issubclass(animal.__class__,Animal))