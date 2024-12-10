import numpy as np
import matplotlib.pyplot as plt

# variables for the simulation
radius = 3.5
rpm = 150
angle = 15
gravity = 9.81
height = 0

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