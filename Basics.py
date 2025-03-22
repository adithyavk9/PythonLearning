day = 21
month = 'september'
temp = 34
print(f"Today is {month} {day} and temperature is {temp}")
light_is_on = True
if light_is_on:
    print("The light is ON!")
print("The light is OFF!") 

####################################

#magic 8 ball
import random
result = random.randint(1,3)
if result == 1:
    print("Yes")
elif result == 2:
    print("No")
else:
    print("May be")

###############################
##list
movies = ["Iron Man" ,"Spider Man","Dune"]
print(movies)
print(movies[1])
movies.append("Thor")
print(movies)
movies.insert(1,"Doctor Strange")
print(movies)
print(len(movies))
del(movies[4])
print(movies)
print(len(movies))
###################################
##for loop 
for number in range(10):
    print("Hello !")
    print("Hi there !")
    print(number)
########################
movies = ["Iron Man" ,"Spider Man","Dune"]
for i in movies:
    print(i)
for i in range(3):
    print(movies[i])
############################
for i in range(40):
    print((i+1) * 2)
############
cats = {"Jane":6, "Tom":14, "Sara":8}
print(cats)
print(cats["Tom"])
cats["Wilson"] = 1
print(cats)
del(cats["Sara"])
##################################
text = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference."""
print(text)
print(len(text)) #number of characters
print(text.split()) #split into list of words
word_count = {}
for word in text.lower().split(): #convert everything to lower case
    #print(i)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
print(word_count["and"])

#########################################
#functions
def bark():
    print("Woof woof!")
bark() #calling function
bark()
bark()
for x in range(100):
    bark()
##################################
def hello(name):
    print(f"Hello {name}")
#hello() must pass a parameter
hello("Adithya")
hello("Meenu")
####################################
def dog_info(name,age):
    print(f"My name is {name} and I am {age}")
dog_info("Rocky",2)
#################################
def double(number):
    return number*2
new_number = double(5)
print(new_number)
##############################
def caps(word):
    out = word.upper()
    return out
caps("meenu")
names = ["nick","joe","rose","chandler"]
for name in names:
    print(caps(name))
###################################
#input
input('Enter some text: ') #input always comes in as string
num = input('Enter a number: ')
print(num * 2)
#########################################




text = input("Enter a text: ")
fun = input("Enter 1 for uppercase and 2 for lower case: ")
out = ''
if int(fun) == 1:
    out = text.upper()
elif int(fun) == 2:
    out = text.lower()
else:
    out = "Invalid Operation"
print(out)

########################################
import random
guess = input("Guess a number between 1 and 100 : \n")
number = random.randint(1,100)
if guess == number:
    print("Congratulations! You have guessed correctly!")
elif guess < number < 100:
    print("Too low! Try again")
elif guess > number > 0:
    print("Too high! Try again")
else:
    print("Not a valid guess")