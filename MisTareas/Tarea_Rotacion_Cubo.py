import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def rotar_x(puntos, angulo):
    rad = np.radians(angulo)
    matriz = np.array([
        [1, 0, 0],
        [0, np.cos(rad), -np.sin(rad)],
        [0, np.sin(rad), np.cos(rad)]
    ])
    return np.dot(puntos, matriz.T)

def rotar_y(puntos, angulo):
    rad = np.radians(angulo)
    matriz = np.array([
        [np.cos(rad), 0, np.sin(rad)],
        [0, 1, 0],
        [-np.sin(rad), 0, np.cos(rad)]
    ])
    return np.dot(puntos, matriz.T)

def rotar_z(puntos, angulo):
    rad = np.radians(angulo)
    matriz = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])
    return np.dot(puntos, matriz.T)

# Definir un cubo
cubo = np.array([
    [0,0,0],
    [1,0,0],
    [1,1,0],
    [0,1,0],
    [0,0,1],
    [1,0,1],
    [1,1,1],
    [0,1,1]
])

caras = [
    [cubo[0], cubo[1], cubo[2], cubo[3]],
    [cubo[4], cubo[5], cubo[6], cubo[7]],
    [cubo[0], cubo[1], cubo[5], cubo[4]],
    [cubo[2], cubo[3], cubo[7], cubo[6]],
    [cubo[1], cubo[2], cubo[6], cubo[5]],
    [cubo[4], cubo[7], cubo[3], cubo[0]]
]

# --- Interacción con usuario ---
eje = input("Eje de rotación (x, y, z): ").lower()
angulo = float(input("Ángulo en grados: "))

if eje == "x":
    cubo_rotado = rotar_x(cubo, angulo)
elif eje == "y":
    cubo_rotado = rotar_y(cubo, angulo)
elif eje == "z":
    cubo_rotado = rotar_z(cubo, angulo)
else:
    print("Eje inválido.")
    exit()

caras_rotadas = [
    [cubo_rotado[0], cubo_rotado[1], cubo_rotado[2], cubo_rotado[3]],
    [cubo_rotado[4], cubo_rotado[5], cubo_rotado[6], cubo_rotado[7]],
    [cubo_rotado[0], cubo_rotado[1], cubo_rotado[5], cubo_rotado[4]],
    [cubo_rotado[2], cubo_rotado[3], cubo_rotado[7], cubo_rotado[6]],
    [cubo_rotado[1], cubo_rotado[2], cubo_rotado[6], cubo_rotado[5]],
    [cubo_rotado[4], cubo_rotado[7], cubo_rotado[3], cubo_rotado[0]]
]

# --- Graficar ---
fig = plt.figure(figsize=(10,5))

# Cubo original
ax1 = fig.add_subplot(121, projection='3d')
ax1.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))
ax1.set_title("Cubo Original")
ax1.set_xlabel("X"); ax1.set_ylabel("Y"); ax1.set_zlabel("Z")
ax1.set_xlim(-2,2); ax1.set_ylim(-2,2); ax1.set_zlim(-2,2)

# Cubo rotado
ax2 = fig.add_subplot(122, projection='3d')
ax2.add_collection3d(Poly3DCollection(caras_rotadas, facecolors='lime', linewidths=1, edgecolors='b', alpha=0.5))
ax2.set_title(f"Cubo Rotado {angulo}° en eje {eje.upper()}")
ax2.set_xlabel("X"); ax2.set_ylabel("Y"); ax2.set_zlabel("Z")
ax2.set_xlim(-2,2); ax2.set_ylim(-2,2); ax2.set_zlim(-2,2)

plt.show()