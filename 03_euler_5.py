#Tom Mirrington
#solution to https://projecteuler.net/problem=5

#determine initial values 
n = 20 
y = 1 # used as a counter, set to 1 to satisfy condition that y > 0

while y > 0:
 y = 0 
 for x in range(1, 21): 
     y = y + (n % x)
 if y == 0:
    print('The smallest positive number that is divisible by 20 is {}'.format(n))
 else:
    n = n + 20 #must be a factor of 20 so increment by 20 to speed up process
    print(n)

#The smallest positive number that is divisible by 20 is 232792560
