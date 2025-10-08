import matplotlib.pyplot as plt
from math import sin, cos, radians

x = [-10, 10, 10, -10, 0]
y = [-10, -10, 10, 10, 0]
z = [-10, -10, -10, -10, 15]
edges = [(0,1),(1,2),(2,3),(3,0),(0,4),(1,4),(2,4),(3,4)]

def rotate(xp, yp, zp, Rx, Ry, Rz):
    y1 = yp*cos(Rx) - zp*sin(Rx)
    z1 = yp*sin(Rx) + zp*cos(Rx)
    x2 = xp*cos(Ry) + z1*sin(Ry)
    z2 = -xp*sin(Ry) + z1*cos(Ry)
    x3 = x2*cos(Rz) - y1*sin(Rz)
    y3 = x2*sin(Rz) + y1*cos(Rz)
    return x3, y3, z2

def draw_pyramid(Rx, Ry, Rz):
    plt.clf()
    plt.axis([-20,20,-20,20])
    plt.axis("off")
    plt.title("Hidden Line Removal – Pyramid")
    coords = [rotate(x[i], y[i], z[i], Rx, Ry, Rz) for i in range(5)]
    for e in edges:
        zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
        if zmean > 0:
            plt.plot([coords[e[0]][0], coords[e[1]][0]],
                     [coords[e[0]][1], coords[e[1]][1]], 'k', lw=2)
    plt.pause(0.001)

plt.ion()
Rx = Ry = Rz = 0
draw_pyramid(Rx, Ry, Rz)
print("=== HLPYRAMID ===")
while True:
    s = input("\nSumbu (x/y/z/q): ").lower()
    if s == "q": break
    a = radians(float(input("Sudut rotasi (°): ")))
    if s == "x": Rx += a
    elif s == "y": Ry += a
    elif s == "z": Rz += a
    draw_pyramid(Rx, Ry, Rz)
plt.ioff()
plt.show()
