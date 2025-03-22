#Ask for name 

name = input("What is your name ? ")

#Ask for  age

age = input("How old are you ? ")

#Ask for city 

city = input("Where do you hail from ? ")

#Ask for hobby 

hobby = input("What are your hobbies ? ")

print("=" * 20)

output = print(f"I am {name}, {age} years old. I hail from {city}. I enjoy {hobby}!")

string = "I am {0}, {1} years old. I hail from {2}. I enjoy {3}!"

out = string.format(name,age,city,hobby)

print(out)


#methods
#string.method()

"hello".count("e")
text = "Happy birthday to you"
text.count("a")
text.count("day")
text = "Happy Birthday"
text.lower()
text.upper()
text #strings are immutable data type 
text.capitalize()#first letter alone caps
text.title()#capitalise start of every word
x = text
x.islower()
x.isalpha()#check if alphabets ; throws false since text has space 
x.isdigit()
x.isalnum()#alphanumeric check
x.index("Birthday")#index of where the string starts
x.index("scghvhxg")#gives error : used when you want a hard stop
x.find("Birthday")
x.find("ndvhcgvdshcgd")#gives -1 : used when you dont want your system to crash
y = "0000000000000000Adithya00000000000000"
y.strip("0")
y.rstrip("0")
y.lstrip("0")
y.strip()#trims extra spaces



name = input("What is your name ? ")
len(name)
name1 = input("What is your name ? ").strip()
len(name1)


#slicer
word = "supercalifragilisticexpialidocious" #iterable data type
word[0]
word[3]
#slicer
#variable[start:end:step]
word[0:5:1]
word[5:9:1]
word[5:]
word[5::2]
word[::-1]
word[:7]

word[-2]
word.index("cali")
word[word.index("cali"):word.index("fragi"):1]