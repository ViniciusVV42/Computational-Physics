import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# ESFERA
# ==========================================

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

r = 1

x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))

# ==========================================
# FIGURA
# ==========================================

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

sphere = ax.plot_surface(
    x, y, z,
    color='royalblue',
    edgecolor='none'
)

# Remove eixos, grade e números
ax.set_axis_off()

# Mantém a esfera perfeitamente circular
ax.set_box_aspect([1, 1, 1])

# ==========================================
# ANIMAÇÃO
# ==========================================

def rotate(frame):

    ax.view_init(
        elev=20,
        azim=frame
    )

    return sphere,

animation = FuncAnimation(
    fig,
    rotate,
    frames=np.arange(0, 360, 2),
    interval=50,
    blit=False
)

plt.show()