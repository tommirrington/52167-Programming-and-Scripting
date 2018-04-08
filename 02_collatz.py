# Tom Mirrington 2018-02-12
# Ecercise 2 submission

#propmpt user for an integer
n = int(input("Please enter a positive integer: "))

while n >= 1: #satisfies the condition that n is a positive integer
    if n == 1: 
        break
    elif n % 2 == 0: #determines if the value is an even number, if even then divide by 2
        n = int(n/2)
        print(n)
        
    else: #if the value is not an even number or 1 then it must be odd therefore multiply by three and add one
        n = (n * 3) + 1
        print(n)
     

#References
#Collatz Conjecture https://en.wikipedia.org/wiki/Collatz_conjecture
#GMIT 52167 Programming and Scripting course material https://learnonline.gmit.ie/course/view.php?id=3940
#The Python Tutorial https://docs.python.org/3/tutorial/
