# Chapter 6 – Hidden Line Removal: Sphere (HLSphere)

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

def rotate(xp, yp, zp, Rx, Ry, Rz):
    y1 = yp*cos(Rx) - zp*sin(Rx)
    z1 = yp*sin(Rx) + zp*cos(Rx)
    x2 = xp*cos(Ry) + z1*sin(Ry)
    z2 = -xp*sin(Ry) + z1*cos(Ry)
    x3 = x2*cos(Rz) - y1*sin(Rz)
    y3 = x2*sin(Rz) + y1*cos(Rz)
    return x3, y3, z2

def make_sphere(n=20, r=10):
    pts = []
    for i in range(n+1):
        theta = np.pi * i / n
        for j in range(n+1):
            phi = 2*np.pi * j / n
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            pts.append((x, y, z))
    edges = []
    for i in range(n):
        for j in range(n):
            a = i*(n+1)+j
            b = a+1
            c = a+(n+1)
            edges.append((a,b))
            edges.append((a,c))
    return pts, edges

def draw_sphere(Rx, Ry, Rz):
    plt.clf()
    plt.axis([-12,12,-12,12])
    plt.axis("off")
    plt.title("Hidden Line Removal – Sphere")
    pts, edges = make_sphere()
    coords = [rotate(p[0],p[1],p[2],Rx,Ry,Rz) for p in pts]
    for e in edges:
        zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
        if zmean > 0:
            plt.plot([coords[e[0]][0], coords[e[1]][0]],
                     [coords[e[0]][1], coords[e[1]][1]], 'k', lw=1)
    plt.pause(0.001)

plt.ion()
Rx = Ry = Rz = 0
draw_sphere(Rx, Ry, Rz)
print("=== HLSphere ===")
print("Masukkan sumbu rotasi (x/y/z), atau q untuk keluar.")
while True:
    s = input("\nSumbu (x/y/z/q): ").lower()
    if s == "q": break
    try:
        a = radians(float(input("Sudut rotasi (derajat): ")))
    except ValueError:
        continue
    if s == "x": Rx += a
    elif s == "y": Ry += a
    elif s == "z": Rz += a
    draw_sphere(Rx, Ry, Rz)
plt.ioff()
plt.show()
