
#inheritance
import random

#general class
class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent!")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

#pound class inherit from the coin class
#pound class get all the methods from coin class flip,clean etc
class Pound(Coin): 
   def __init__(self):
       data = {
          "original_value":1.00,
          "clean_colour":"gold",
          "rusty_colour":"greenish",
          "num_edges":1,
          "diameter":22.5,
          "thickness":3.15,
          "mass":9.5
        }
       super().__init__(**data)#pass as keyword arg 
    #instead of writing self. we want parent class to take care of everything
    #so we go inside init function of child class and we run the parent's init #function and pass it this dictionary
    #to run parent's init we need to access the parent class, we use the super
    #class to do that
    #

one_pound_coin = Pound()
one_pound_coin.colour
one_pound_coin.rust()
one_pound_coin.colour
    