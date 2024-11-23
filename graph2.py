import matplotlib.pyplot as plt
import numpy as np

xmin=-20
xmax=20
ymin=-20
ymax=20
points=5 * (xmax-xmin)

x=np.linspace(xmin,xmax,points)
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0], 'black')
plt.plot([0,0],[ymin,ymax],'black')

ax.set_xlabel('x values')
ax.set_ylabel('y values')
ax.set_title('Some Graph')
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,2))
ax.set_yticks(np.arange(ymin,ymax,2))

y= 2* x +1
plt.plot(x,y,label='y=2* x +1')
plt.plot(4,6,'bX',label='points')
plt.plot(x*3,x*2,'darkblue',label='steeper line')


plt.legend()

plt.show()

