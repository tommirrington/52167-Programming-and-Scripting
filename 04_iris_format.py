#Tom Mirrigton
#Exercise 5 submission

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      print('petal length: {0} petal width: {1} sepal length: {2} sepal width: {3}'.format(x[0],x[1],x[2],x[3]))
