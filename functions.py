#functions
#define
def add(x,y):
    x + y
#return
    return x + y 
#call the function
add(5,10)

#returning is not same as print
#print just show value on the screen - will not store value in comp memory

def add(x,y):
#print
    print(x + y )
answer = add (5,7)
type(answer)

#reverse string
def invert_string(x):
    answer = x[::-1]
    return answer

invert_string("adithya")

################################################################################################################################################################
#variable scope
#two types
#global scope and local scope
#functions create local scope

a = 100  #here 'a' has global scope

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()

#######
#funtions create local scopes
def f1():
    b = 100  #here 'b' has local scope
    print(b)

def f2():
    b = 100
    print(b)

f1()
f2()

############
def f1():
    b = 100  #here 'b' has local scope
    print(b)

def f2():
    b = 80 #local scope
    print(b)

f1()
f2()

####################
#when function tries to modify global variable from inside a local scope python #stops that from happening by creating a local variable in same name. 
#these variable are destroyed once the function run is completed
#we can use global variable inside function not change it.
b = 250 
def f1():
    b = 100  #here 'b' has local scope
    print(b)

def f2():
    b = 80
    print(b)

f1()
f2()
print(b)


###################################

#how to overwrite the global variable from local scope
b = 250 
def f1():
    global b
    b = 100  #here 'b' has global scope
    print(b)

def f2():
    b = 80 #local scope
    print(b)

f1()  
f2()
print(b)


#we cannt overwrite global list variable from inside a function
#but we can change an element from list.
b = [1,2,3] 
def f1():
    b = 100  
    print(b)

def f2():
    b = 80 #local scope
    print(b)

f1()  
f2()
print(b)

#####
b = [1,2,3] 
def f1():
    b[0] = 100  
    print(b)

def f2():
    b = 80 #local scope
    print(b)

f1()  
f2()
print(b)


#####
def about(name,age,likes): #parameter is wat we use in function defenition
    sentence = "Meet {}! They are {} years old and they like {}!".format(name,age,likes)
    return sentence
#positional arguments
about("jack",23,"python") #arguments is what we pass to function when we call it
#key word arguments
about(age=23,likes="python",name="rose")


about("jack",23)#will throw error unless we give it a default value in the definition
def about(name,age,likes = "Football"): #default parameter has to go last
    sentence = "Meet {}! They are {} years old and they like {}!".format(name,age,likes)
    return sentence
about("jack",23) #will now run without error




############################################

#packing and unpacking 

print(1,2,3,4)
numbers = [1,2,3,4]
print(numbers)
print(*numbers) #unpack argument : numbers
#can unpack any iterable data type before printing
print(*"abc")


#packing arguments
#happens inside functions
#useful when not sure about the number of arguments

def add(x,y):
    return x+y
add(10,10) #can add only 2 numbers


def add(*numbers): #can add any number of numers
    total = 0
    for number in numbers:
        total += number
    return total

add(1,2,3,4,5,5)

#keyword arguments
def about(name,age,likes): #parameter is wat we use in function defenition
    sentence = "Meet {}! They are {} years old and they like {}!".format(name,age,likes)
    return sentence

dictionary = {"age":23,"likes":"python","name":"rose"}
about(**dictionary) #2 stars for keyword arg unpacking


#pack keyword arg
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

foo(huda = "Female", ziyad = "male")


 