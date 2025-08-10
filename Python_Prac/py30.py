import numpy as np
z = 1 + 0j  # start along the real axis
theta_deg = 90
theta_rad = np.deg2rad(theta_deg)
rotated_z = z*np.exp(1j*theta_rad*2)
rotated_angle = np.angle(rotated_z, deg=True)
print("Rotated Z:", rotated_angle)
   


