# Tom Mirrington 2018-02-12
# Ecercise 2 submission

#prompt user for an integer
n = int(input("Please enter a positive integer: "))


#satisfy the condition that n is a positive integer
#determine if the value is an even number, if even then divide by 2
#if the value is not an even number or 1 then it must be odd therefore multiply by three and add one

while n >= 1: 
    if n == 1: 
        break
    elif n % 2 == 0: 
        n = int(n/2)
        print(n)
        
    else: 
        n = (n * 3) + 1
        print(n)
     

#References
#Collatz Conjecture https://en.wikipedia.org/wiki/Collatz_conjecture
#GMIT 52167 Programming and Scripting course material https://learnonline.gmit.ie/course/view.php?id=3940
#The Python Tutorial https://docs.python.org/3/tutorial/
