##animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##is-a
class Dog(Animal):

    def __init__(self, name):
        ##has-a
        self.name = name

##is-a
class Cat(Animal):

    def __init__(self, name):
        ##has-a
        self.name = name

##is-a
class Person (object):

    def __init__(self, name):
        #has-a
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##is-a
class Employee(Person):

    def _init_(self, name, salary):
        ##has-a
        super(Employee, self)._init_(name)
        ##has-a
        self.salary = salary

##is-a
class Fish(object):
    pass

##is-a
class Salmon (Fish):
    pass

##
class Halibut (Fish):
    pass


##
rover = Dog("Rover")

##
satan = Cat("Satan")

##
mary = Person ("Mary")

##
mary.pet = satan

##
frank = Employee("Frank", 120000)

##
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()
