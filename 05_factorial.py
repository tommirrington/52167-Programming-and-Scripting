#Tom Mirrigton
#Exercise 6 submission

#define the function factorial

def fact(x):
    y = 1 #must start at 1 or for loop will just multiply through 0
    for i in range (1, x + 1):
        y = y * i
    return y

#test function 

m = 5
n = 7
p = 10

print(fact(m))
print(fact(n))
print(fact(p))
