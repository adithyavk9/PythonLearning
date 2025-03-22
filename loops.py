#while  
#repeat code while the condition is true
count = 0
while count < 10:
    print("Hello")
    count += 1
######
x = 1
while x<= 10:
    print(x)
    x += 1

#######
#baby
from random import choice
questions = ["Why is sky the blue?","Why is there a face on moon?","Where are all the dinosaurs?"]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("Why!!!!!!!!!!!").strip().lower()




#for
#range
for i in range(1,14):
    print(i)
#string
for letter in "abcd":
    print(letter)


#counting vowels
vowels = 0
consonants = 0

for i in "Bicycles ".strip().lower():
    if i in "aeiou":
        vowels += 1 
    else:
        consonants +=1
print(f"Vowels : {vowels}  Consonants : {consonants}")


#dictionary
#print names with a in it
students = {
    "male": ["John", "Michael", "David", "James"],
    "female": ["Emma", "Sophia", "Olivia", "Ava"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)


