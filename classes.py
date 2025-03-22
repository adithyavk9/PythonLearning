#classes
import random
class Dog:
    info = "Bow Bow" #class variable

    def __init__(self):  #init -- initialisation function. whenever a new #object is created from class this function gets called
        print("I am alive!")
        print(random.randint(1,10))
        #instance variables
        self.lucky_number = random.randint(1,10)
print(Dog.info) 

Dog() #created an individual object from the class
Dog()
dog1 = Dog()
dog2 = Dog()
print(dog1.lucky_number)
print(dog2.lucky_number)

#method is a function inside a class
