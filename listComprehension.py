#list comprehension
#list with even numbers between 0 and 100 
even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

#string list 
words = ["the","quick","brown","fox","jumps"]
answer = [[w.upper(),w.lower(),len(w)] for w in words]
print(answer)

