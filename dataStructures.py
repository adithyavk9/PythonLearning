#lists
#iterable data structures
our_list = ["A", "B", 1, 2, True, False]
our_list[0]
x = our_list[-2]
print(x)

#slicers - just take a copy will not modify the original list
our_list[0:5:1]

list_new = [1, 2, [3, 4, 5], 9]
list_new[2]
list_new[2][1]
list_new[2][1:]
del list_new[0]
del list_new[0:2]


###travis security system project

known_users = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name? : ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?").strip().lower()
        if remove =="y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        else :
            print("No problem, I didn't want you to leave me anyway!")
    else:
        print("I don't think I have met you before {}!".format(name))
        add_me = input("Would you like to be added to the system (y/n)?").strip().lower()
        if add_me =="y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        else:
            print("No worries, see you around!")


##################

#addition operator
A = [3, 5, 6, 7]
A + [1] #can only add list to list
A + ['BCD']
A + list("BCD")#add elements one by one
A + list("123") #will not work as numbers are not iterable
A + list(str(123)) #can convert to string 
#list as an element
A + [[1,2,3]]
A.append([8])#append method returns an empty value
A.append(10)#will give empty spaces
type(A)
#insert at any point
B = [2, 4, 6, 8, 9]
B.insert(2,[2, 4])
B
#lists are mutable
B.remove(8)
B


#####################
#tuples
#immutable
our_tuple = (1,2,3,"A","B")
type(our_tuple)
our_tuple[0:3]
#cannt change our_tuple[1]=100 will throw error
A,B,C=1,2,3
D,E,F=[4,5,6]
G,H,I="789"


#################################
#dictionary
#has no order
#always access using keys not index
students = {"Alice":25, "Bob":30, "Charlie":28, "David":27, "Emma":25}
students["David"]
students["Fred"]=25
students["Alice"]=26
del students["Fred"]
students.keys()
students.values()
students.items()

#keys with multiple values
students = {"Alice":["ID0001", 25, "A"], 
            "Bob":["ID0002", 30, "B"] , 
            "Charlie":["ID0003", 28, "C"] , 
            "David":["ID0004", 27, "D"] , 
            "Emma":["ID0005", 25, "E"] }
print(students["Alice"])
print(students["Alice"][0])
print(students["Bob"][1:])
  
students_new = {
            "Alice":{"id":"ID0001", "age": 25,"grade" : "A"}, 
            "Bob":{"id":"ID0002", "age": 30,"grade" : "B"}, 
            "Charlie":{"id":"ID0003", "age": 28,"grade" : "C"}
            }
students_new["Alice"]["age"]
students_new["Bob"]["age"],students_new["Bob"]["grade"]




