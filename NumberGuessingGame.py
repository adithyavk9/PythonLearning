import random
number = random.randint(1,100)
print(number)
guess = int(input("Guess a number between 1 and 100 : \n"))
count = 0
for i in range(1,100):
    count += 1 
    if number == guess:
        print(f"Good job! You have guessed the number right! You have guessed in {count} tries!")
        break
    elif guess < number:
        print("Too low! Guess Again")
    elif guess > number:
        print("Too high! Guess Again")
    guess = int(input("Guess a number between 1 and 100 : \n"))



########################################
import random
number = random.randint(1,100)
print(number)
guess = int(input("Guess a number between 1 and 100 : \n"))
count = 1
while number != guess:
    count += 1 
    if guess < number:
        print("Too low! Guess Again")
    elif guess > number:
        print("Too high! Guess Again")
    guess = int(input("Guess a number between 1 and 100 : \n"))
print(f"Good job! You have guessed the number right! You have guessed in {count} tries!")
      