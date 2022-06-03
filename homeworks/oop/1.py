#from re import A


class Animal:
    def eat(self):
        pass

    def sleep(self):
        pass

class Worm(Animal):
    def poop(self):
        pass

class Dog(Animal):
    def run(self):
        pass

class Cat(Animal):
    def scratch(self): 
        pass

class Bird(Animal):
    def fly(self):
        pass

    def stuck_in_mouth(self):
        pass

class Tree():
    def grow_up(self):
        pass

worm = Worm()
cat =Cat()
dog = Dog()
bird= Bird()
tree = Tree()

class Horce(Animal):
    def run_on_4_legs(self):
        pass
    def kick_with_2_legs(self):
        pass

class Human(Animal):
    def study(self):  pass

    def work(self):
        print("doing hard job")

class Centaur(Human,Horce):
    def shoot_on_run(self):
        pass


creature = Centaur()
creature.kick_with_2_legs()
creature.shoot_on_run()
creature.kick_with_2_legs()
creature.work()

for animal in (worm,cat,dog,bird,tree,creature):
    print(animal.__class__.__name__, "Is animal subclass :",issubclass(animal.__class__,Animal))