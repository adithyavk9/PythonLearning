#welcome mat - my code 
n = 9
m = 3*n
for i in range(n):
    if i == (n-1)/2:
        print("-"*int((m-7)/2)+"WELCOME"+"-"*int((m-7)/2))
    elif i < (n-1)/2:
        print("-"*(int((m-(i*2+1)*3)/2))+".|."*(i*2+1)+"-"*(int((m-(i*2+1)*3)/2)))
    else:
        i = int(n-1/2) - i
        print("-"*(int((m-(i*2+1)*3)/2))+".|."*(i*2+1)+"-"*(int((m-(i*2+1)*3)/2)))

#code
n , m = tuple(map(int, input().split()))
j = 2
for i in range(n):
    if i < n // 2:
        f = ".|." + ".|."*(j*i)
        print(f.center(m, "-"))
    elif i == n // 2:
        print("WELCOME".center(m, "-"))
    elif i > n // 2:
        f = ".|." * (n - j)
        print(f.center(m, "-"))
        j += 2