
#pig latin converter
# pig --> igPay consonants
#apple --> appleyay vowels

#get sentence from user
original = input("Enter a sentence : ").strip().lower()

#split sentence into words
words = original.split()
print(words)

#loop and convert to pig latin
new_word = []
for x in words:
    
    if x[0] in "aeiou":
        new_word.append(x + "yay")
        
    else:
        new = []
        y = list(x)
        
        for i in x:
            
            if i not in "aeiou":
                y.remove(i)
                print(y)
                new.append(i)
                print(new)
            else:
                break
        word_pig = y + new + list("ay")
        new_word.append(''.join(word_pig))
print(' '.join(new_word))

#stick words back together

#ouput the final string
