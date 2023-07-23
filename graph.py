import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math

# parameters
dt = 0.01
epsilon = 0.01
v = 1

# variables
c = 1
A = [np.array((0, 0))]
B = [np.array((1, 0))]
C = [np.array((1, 1))]
D = [np.array((0, 1))]
curves = [A, B, C, D]

# Utility fonctions
def norm(v):
    return math.sqrt(v[0]**2+v[1]**2)

def normalize(v):
    return v/norm(v)

# Main loop
while c > epsilon:
    newPoints = []
    for i, curve in enumerate(curves):
        next_curve = curves[(i+1)%4]
        firstPoint = curve[-1]
        secondPoint = next_curve[-1]
        direction = secondPoint - firstPoint
        c = norm(direction)
        direction = normalize(direction)
        direction *=  v*dt
        newPoints.append(firstPoint+direction)
    for i, point in enumerate(newPoints):
        curves[i].append(point)

# Define plot
A_vect = np.array(A)
B_vect = np.array(B)
C_vect = np.array(C)
D_vect = np.array(D)
fig, ax = plt.subplots()

ax.set_aspect('equal')
plt.subplots_adjust(bottom=0.2)

def draw_curves():
    ax.plot(A_vect[:, 0], A_vect[:, 1])
    ax.plot(B_vect[:, 0], B_vect[:, 1])
    ax.plot(C_vect[:, 0], C_vect[:, 1])
    ax.plot(D_vect[:, 0], D_vect[:, 1])

def draw_square(i):
    i = int(i)
    ax.clear()
    draw_curves()
    square = plt.Polygon(np.array([A_vect[i], B_vect[i], C_vect[i], D_vect[i]]), fill=False, ec="brown")
    ax.add_patch(square)

# Add slider
axslider = plt.axes([0, 0, 1, 0.1])
iteration = Slider(axslider, 'Iteration', 0, len(A_vect))
iteration.on_changed(draw_square)

# Plot
draw_curves()
plt.show()