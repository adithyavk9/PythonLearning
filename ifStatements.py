#if statement runs only if condition returns true
#if condition:
#   statement
if 2 > 3:
    print("It will not  run")
if 20 > 3:
    print("It will run")

#else conditions runs if condition is false
num1 = 10
num2 = 23
if num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is lesser than num2")
else:
    print("both numbers are equal")
#logical operator
not False
not True
c = 10
d = 5
if c > 10 and d> 1:
    print("It worked")