#objects and classes
#classes are like templates
#we use it to make objects/instances
#classes are made up of variables/states and functions/methods
 
class Pound: #defining class

    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True

#object
coin1 = Pound()
print(coin1.value)

type(coin1)

coin1.colour = "greenish" #only change for object coin1
print(coin1.colour)


#objects can behave independently
coin2 = Pound()
print(coin2.colour)



#methods
#to create methods we need a constructor
#defined as def __init__(self)
#self is wat we used to refer to the specific instance of the class when we write the class code

import random
class Pound: #defining class

    def __init__(self,rare=False): #can have more than one parameter

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    #destructor
    def __del__(self):
        print("Coin spent!")


    def rust(self):
        self.colour = "greenish"
    
    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice


coin1 = Pound(rare=True)
coin2 = Pound()
coin1.rare
coin2.rare
coin1.value
coin2.value
coin1.rust()
coin1.colour
coin1.clean()
coin1.colour
del coin1
