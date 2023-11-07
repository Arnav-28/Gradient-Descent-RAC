import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set data points 
x = np.linspace(0,20,60)
y = 2*x**2 - np.random.uniform(-5, 5, 60)*x + np.random.uniform(-20, 20, 60)

#Let the equation be y = ax^2 + bx + c
a=0
b=0
c=0
learningRate = 0.00001

#Gradient descent for regression
for i in range (200):
    da = 0.0
    db = 0.0
    dc = 0.0

    for xi,yi in zip(x,y):
        da += -2 * xi**2 * (yi - a * xi**2 + b * xi + c)
        db += -2 * xi * (yi - a * xi**2 + b * xi + c)
        dc += -2 * (yi - a * xi**2 + b * xi + c)

    a -= (learningRate * da)/len(x)
    b -= (learningRate * db)/len(x)
    c -= (learningRate * dc)/len(x)
print(a,b,c)
x_curve = np.linspace(0, 22, 65)
y_curve = a * x_curve**2 + b * x_curve + c

next_x_points = x_curve[-5:]
next_y_points = y_curve[-5:]

#Presentation of best fit curve and next 5 points(in green)
plt.scatter(x, y, label='Data Points')
plt.scatter(next_x_points, next_y_points, color='green')
plt.plot(x_curve, y_curve, color='red', label='Quadratic Curve')

# Animation

fig, ax = plt.subplots()
ax.set_xlim(0, 25) 
ax.set_ylim(0, 1000)

ax.scatter(x, y, color='red', label='Data Points')

x_plot = np.linspace(0, 25, 100)
y_plot = a * x_plot**2 + b * x_plot + c
line, = ax.plot([], [], lw=2)

def animate(frame):
    if frame < len(x_plot):
        line.set_data(x_plot[:frame], y_plot[:frame])
        return line,

num_frames = len(x_plot)
ani = FuncAnimation(fig, animate, frames=num_frames, repeat=True, blit=True)
plt.show()

ani.save("quadraticAnimation.gif", writer="pillow") 