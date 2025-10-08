"""
PERSPECTIVE — contoh proyeksi perspektif kubus 3D
Berdasarkan Chapter 8 dari 'Python Graphics: A Reference for Creating 2D and 3D Images'
"""

import matplotlib.pyplot as plt
from math import sin, cos, radians

# Titik-titik kubus
x = [-10, 10, 10, -10, -10, 10, 10, -10]
y = [-10, -10, 10, 10, -10, -10, 10, 10]
z = [10, 10, 10, 10, -10, -10, -10, -10]

# Parameter proyeksi
d = 50   # jarak pandang
xc, yc = 75, 50

# Fungsi rotasi
def rotx(xp, yp, zp, Rx):
    y2 = yp*cos(Rx) - zp*sin(Rx)
    z2 = yp*sin(Rx) + zp*cos(Rx)
    return xp, y2, z2

def roty(xp, yp, zp, Ry):
    x2 = xp*cos(Ry) + zp*sin(Ry)
    z2 = -xp*sin(Ry) + zp*cos(Ry)
    return x2, yp, z2

def rotz(xp, yp, zp, Rz):
    x2 = xp*cos(Rz) - yp*sin(Rz)
    y2 = xp*sin(Rz) + yp*cos(Rz)
    return x2, y2, zp

# Fungsi proyeksi perspektif
def perspective(xp, yp, zp):
    scale = d / (d + zp)
    xp2 = xc + xp * scale
    yp2 = yc - yp * scale
    return xp2, yp2

# Fungsi plot
def plot_cube(Rx=0, Ry=0, Rz=0):
    plt.clf()
    plt.axis([0, 150, 100, 0])
    plt.grid(True)
    plt.title("Perspective Projection — Rotating Cube")

    xg, yg, zg = [], [], []
    for i in range(8):
        xp, yp, zp = x[i], y[i], z[i]
        xp, yp, zp = rotx(xp, yp, zp, Rx)
        xp, yp, zp = roty(xp, yp, zp, Ry)
        xp, yp, zp = rotz(xp, yp, zp, Rz)
        xg.append(xp)
        yg.append(yp)
        zg.append(zp)

    # Gambar sisi-sisi kubus
    edges = [(0,1),(1,2),(2,3),(3,0),
             (4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]

    for e in edges:
        x1, y1 = perspective(xg[e[0]], yg[e[0]], zg[e[0]])
        x2, y2 = perspective(xg[e[1]], yg[e[1]], zg[e[1]])
        plt.plot([x1, x2], [y1, y2], 'k', lw=2)

    plt.pause(0.001)

# =================== Loop utama interaktif ===================
plt.ion()
Rx = Ry = Rz = 0
plot_cube(Rx, Ry, Rz)

print("=== Program Perspective Cube ===")
print("Ketik sumbu rotasi (x/y/z) atau q untuk keluar.")

while True:
    axis = input("\nSumbu (x/y/z/q): ").strip().lower()
    if axis == "q":
        break
    try:
        angle = float(input("Masukkan sudut rotasi (derajat): "))
    except ValueError:
        continue
    if axis == "x":
        Rx += radians(angle)
    elif axis == "y":
        Ry += radians(angle)
    elif axis == "z":
        Rz += radians(angle)
    plot_cube(Rx, Ry, Rz)

print("Selesai.")
