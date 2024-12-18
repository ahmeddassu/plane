import numpy as np
import matplotlib.pyplot as plt
import aerodynamics as aero
import environment as env

# variables for the simulation
radius = 3.5
rpm = 150
angle = 15
gravity = 9.81
height = 0
wingarea = 5

# calculating the tangential speed (output speed of the plane)
rps = rpm / 60
radps = rps * np.pi * 2
v0 = radius * radps
print(f"tangential speed: {v0:.3f} m/s")

# calculating the angle in radians
radangle = angle * (np.pi / 180)
print(f"angle: {radangle:.3f} rad")

# calculating flight time
time = 2 * (v0 * np.sin(radangle)) / gravity
print(f"total flight time: {time:.3f} seconds")

# calculating velocities
xvelocity = v0 * np.cos(radangle)
print(f"velocity on the x: {xvelocity:.3f} m/s")
yvelocity = v0 * np.sin(radangle)
print(f"velocity on the y: {yvelocity:.3f} m/s")

# calculating the local maximum of the parabola
hmax = (v0 * np.sin(radangle))**2 / (2 * gravity)
print(f"maximum height: {hmax:.3f} meters")

# generate points in time, which are spaced between the total flight time and 0 at regular intervals
timepoints = np.linspace(0, time, 100)

# initialising empty lists to store x and y coordinates
xpositions = []
ypositions = []

# going through each point in time, and calculating the x and y coordinates
for t in timepoints:
    x = xvelocity * t
    y = (yvelocity * t - 0.5 * gravity * t ** 2) + height
    
    altitude = y
    
    drag = aero.drag(wingarea, v0, env.airdensity(env.atmosphericpressure(altitude), env.temperature(altitude)), altitude)
    lift = aero.lift(wingarea, v0, env.airdensity(env.atmosphericpressure(altitude), env.temperature(altitude)), altitude)

    xpositions.append(x)
    ypositions.append(y)

# plotting the trajectory
plt.figure(figsize=(14, 6))
plt.plot(xpositions, ypositions, label="trajectory", color="purple")
plt.title("plane parabola")
plt.xlabel("horizontal distance (m)")
plt.ylabel("verical distance (m)")

plt.show()


'''
TO DO:
1. Make an x, y easy viewer
2. Find glide distances?
3. Add mass and air resistance if possible
'''