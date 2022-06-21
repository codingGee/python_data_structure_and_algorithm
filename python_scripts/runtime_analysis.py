import matplotlib.pyplot as plt
import math 


# create a range of val from 1 to 100 
x = list(range(1, 100))
# create the lists and assign a the val of 1 
l = []; l2=[]; a = 1
# start plotting the graph 
plt.plot(x, [y * y for y in x])
plt.plot(x, [(7 * y)* math.log(y, 2) for y in x])
plt.plot(x, [(6 *y )* math.log(y, 2) for y in x])
plt.show()
