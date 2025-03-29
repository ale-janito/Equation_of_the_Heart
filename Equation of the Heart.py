import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir la ecuación del corazón
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')  # Desactivar los ejes

# Inicializar una línea vacía
line, = ax.plot([], [], color='red')

# Función de inicialización
def init():
    line.set_data([], [])
    return line,

# Función de animación
def animate(i):
    line.set_data(x[:i], y[:i])  # Mostrar una porción del corazón
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, interval=20)

plt.show()
