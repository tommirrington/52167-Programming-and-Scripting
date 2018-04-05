#Tom Mirrigton
#Exercise 6 submission

#define the function factorial

def fact(x):
    y = 1 #must start at 1 or for loop will just multiply through 0
    for i in range (1, x + 1):
        y = y * i
    return y

#test function using input/output

x = int(input("Please enter a positive integer: "))

print(fact(x))


