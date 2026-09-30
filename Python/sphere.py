import numpy as np
import matplotlib.pyplot as plt

# Coordenadas da esfera
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Raio
r = 1

# Coordenadas cartesianas
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))

# Criar figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar esfera
ax.plot_surface(x, y, z)

# Eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mesma escala nos três eixos
ax.set_box_aspect([1, 1, 1])

plt.show()