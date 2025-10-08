import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians

def rotate(xp, yp, zp, Rx, Ry, Rz):
    y1 = yp*cos(Rx) - zp*sin(Rx)
    z1 = yp*sin(Rx) + zp*cos(Rx)
    x2 = xp*cos(Ry) + z1*sin(Ry)
    z2 = -xp*sin(Ry) + z1*cos(Ry)
    x3 = x2*cos(Rz) - y1*sin(Rz)
    y3 = x2*sin(Rz) + y1*cos(Rz)
    return x3, y3, z2

def draw_no_hlr(ax, coords, edges, title):
    ax.clear()
    for e in edges:
        x1, y1, z1 = coords[e[0]]
        x2, y2, z2 = coords[e[1]]
        ax.plot([x1, x2], [y1, y2], 'k', lw=1.5)
    ax.set_title(f"{title}\nTanpa HLR")
    ax.axis("equal")
    ax.axis("off")

def draw_hlr(ax, coords, edges, title):
    ax.clear()
    for e in edges:
        zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
        if zmean > 0:
            x1, y1, z1 = coords[e[0]]
            x2, y2, z2 = coords[e[1]]
            ax.plot([x1, x2], [y1, y2], 'k', lw=1.5)
    ax.set_title(f"{title}\nDengan HLR")
    ax.axis("equal")
    ax.axis("off")

def pyramid_points():
    pts = [(-10,-10,-10),(10,-10,-10),(10,10,-10),(-10,10,-10),(0,0,15)]
    edges = [(0,1),(1,2),(2,3),(3,0),(0,4),(1,4),(2,4),(3,4)]
    return pts, edges, "Pyramid"

def plane_points():
    pts = []
    for i in range(-10, 11, 5):
        for j in range(-10, 11, 5):
            pts.append((i, j, 0))
    edges = []
    for i in range(0, len(pts)-5, 5):
        for j in range(4):
            edges.append((i+j, i+j+1))
    for i in range(5):
        for j in range(0, len(pts)-10, 5):
            edges.append((i+j, i+j+5))
    return pts, edges, "Plane Grid"

def sphere_points(n=20, r=10):
    pts = []
    for i in range(n+1):
        theta = np.pi * i / n
        for j in range(n+1):
            phi = 2 * np.pi * j / n
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
    return pts, edges, "Sphere Wireframe"

def draw_scene(Rx, Ry, Rz, pts, edges, title):
    coords = [rotate(p[0], p[1], p[2], Rx, Ry, Rz) for p in pts]
    draw_no_hlr(ax1, coords, edges, title)
    draw_hlr(ax2, coords, edges, title)
    fig.canvas.draw_idle()
    plt.pause(0.001)

shape = input("Pilih bentuk (pyramid / plane / sphere): ").strip().lower()
if shape == "pyramid":
    pts, edges, title = pyramid_points()
elif shape == "plane":
    pts, edges, title = plane_points()
elif shape == "sphere":
    pts, edges, title = sphere_points()
else:
    print("Bentuk tidak dikenali.")
    exit()

plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle(f"Perbandingan: {title} – Non-HLR vs HLR", fontsize=14)

Rx = Ry = Rz = 0
draw_scene(Rx, Ry, Rz, pts, edges, title)

print(f"=== Program Perbandingan {title} ===")
print("Gunakan sumbu rotasi (x/y/z), q untuk keluar.")

while True:
    s = input("\nSumbu (x/y/z/q): ").lower()
    if s == "q":
        break
    try:
        a = radians(float(input("Sudut rotasi (derajat): ")))
    except ValueError:
        continue
    if s == "x":
        Rx += a
    elif s == "y":
        Ry += a
    elif s == "z":
        Rz += a
    draw_scene(Rx, Ry, Rz, pts, edges, title)

plt.ioff()
plt.show()
