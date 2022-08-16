import numpy as np

x, y, z = 25, 25, 25

v = np.zeros((x, y, z, 3))
n = np.zeros((x, y, z))

n+1 = -(v[x+1, y, z, 0] + v[x-1, y, z, 0] - 2*v[x, y, z, 0])
      -(v[x, y+1, z, 1] + v[x, y-1, z, 1] - 2*v[x, y, z, 1])
      -(v[x, y, z+1, 2] + v[x, y, z-1, 2] - 2*v[x, y, z, 2])
      *dt/dx

v[0]+1 = -(n[x+1, y, z] + n[x-1, y, z] - 2*n[x, y, z]) * k_b*T * dt/dx
v[1]+1 = -(n[x, y+1, z] + n[x, y-1, z] - 2*n[x, y, z]) * k_b*T * dt/dx
v[2]+1 = -(n[x, y, z+1] + n[x, y, z-1] - 2*n[x, y, z]) * k_b*T * dt/dx
