import matplotlib.pyplot as plt
import numpy as np


xmin=-10
xmax=10
ymin=-10
ymax=10



fig, ax = plt.subplots()

plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

print('x \t y')
for x in range(-5,11):
    y= x* 0.3 +2
    plt.plot([x],[y],'rX')
    print(x,'\t', y)



plt.show()