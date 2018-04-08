#Tom Mirrigton
#Exercise 6 submission

#define the function factorial

def fact(x):

#set y to 1 or for loop will just multiply through 0
  
    y = 1 

#for loop using a range of all values up to and including x
#iterating though the for loop will multiply i value by cumaltive y value

    for i in range (1, x + 1): 
        y = y * i 
    return y

#test function using specified values

m = 5
n = 7
p = 10

print(fact(m))
print(fact(n))
print(fact(p))


#References
#GMIT 52167 Programming and Scripting course material https://learnonline.gmit.ie/course/view.php?id=3940
#The Python Tutorial https://docs.python.org/3/tutorial/