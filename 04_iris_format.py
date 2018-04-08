#Tom Mirrigton
#Exercise 5 submission


#open csv data file, for each line split into a list using the ',' delimmiter
#print using list index

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      print('petal length: {0} petal width: {1} sepal length: {2} sepal width: {3}'.format(x[0],x[1],x[2],x[3]))


#References
#GMIT 52167 Programming and Scripting course material https://learnonline.gmit.ie/course/view.php?id=3940
#The Python Tutorial https://docs.python.org/3/tutorial/