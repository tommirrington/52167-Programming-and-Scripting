#Tom Mirrington
#solution to https://projecteuler.net/problem=5

#determine initial values 
#use y as counter, set to 1 to satisfy condition that y > 0

n = 20 
y = 1 

 #reset y to 0 then iterate though range 1 to 20, if the sum of the modulus value for entire range is zero
 #then n is divisible by all values from 1 to 20, if not then increment n by 20 and test again
 #the soolution must be a factor of 20 so increment by 20 to speed up process

while y > 0:
 y = 0 
 for x in range(1, 21): 
     y = y + (n % x) 
 if y == 0:
    print('The smallest positive number that is divisible by all of the numbers from 1 to 20 is {}'.format(n))
 else:
    n = n + 20 
    print(n)

#The smallest positive number that is divisible by all of the numbers from 1 to 20 is 232792560


#References
#GMIT 52167 Programming and Scripting course material https://learnonline.gmit.ie/course/view.php?id=3940
#The Python Tutorial https://docs.python.org/3/tutorial/