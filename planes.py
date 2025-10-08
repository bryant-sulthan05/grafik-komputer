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

def make_plane(zpos=0, shiftx=0, shifty=0):
    pts = []
    for i in range(-10, 11, 5):
        for j in range(-10, 11, 5):
            pts.append((i+shiftx, j+shifty, zpos))
    edges = []
    for i in range(0, len(pts)-5, 5):
        for j in range(4):
            edges.append((i+j, i+j+1))
    for i in range(5):
        for j in range(0, len(pts)-10, 5):
            edges.append((i+j, i+j+5))
    return pts, edges

def draw_two_planes(Rx, Ry, Rz):
    plt.clf()
    plt.axis([-20, 20, -20, 20])
    plt.axis("off")
    plt.title("Hidden Line Removal – Two Planes")

    planes = [
        make_plane(zpos=0),   # bidang depan
        make_plane(zpos=-10)  # bidang belakang
    ]
    for pts, edges in planes:
        coords = [rotate(p[0], p[1], p[2], Rx, Ry, Rz) for p in pts]
        for e in edges:
            zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
            if zmean > 0:
                plt.plot([coords[e[0]][0], coords[e[1]][0]],
                         [coords[e[0]][1], coords[e[1]][1]], 'k', lw=1.5)
    plt.pause(0.001)

plt.ion()
Rx = radians(30)
Ry = radians(30)
Rz = 0
draw_two_planes(Rx, Ry, Rz)

print("=== TWO PLANES ===")
while True:
    s = input("\nSumbu rotasi (x/y/z/q): ").lower()
    if s == "q": break
    try:
        a = radians(float(input("Sudut rotasi (°): ")))
    except ValueError:
        continue
    if s == "x": Rx += a
    elif s == "y": Ry += a
    elif s == "z": Rz += a
    draw_two_planes(Rx, Ry, Rz)
plt.ioff()
plt.show()
