# Tom Mirrington 2018-02-12
# Collatz Conjecture https://en.wikipedia.org/wiki/Collatz_conjecture

#propmpt user for an integer
n = int(input("Please enter a positive integer: "))

while n >= 1:
    if n == 1:
        break
    elif n % 2 == 0:
        n = int(n/2)
        print(n)
        
    else:
        n = (n * 3) + 1
        print(n)
     


