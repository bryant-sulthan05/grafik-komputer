import matplotlib.pyplot as plt
from math import sin, cos, radians

x = [-10, 10, 10, -10, -10, 10, 10, -10]
y = [-10, -10, 10, 10, -10, -10, 10, 10]
z = [10, 10, 10, 10, -10, -10, -10, -10]

edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

def rotate(xp, yp, zp, Rx, Ry, Rz):
    y1 = yp*cos(Rx) - zp*sin(Rx)
    z1 = yp*sin(Rx) + zp*cos(Rx)
    x2 = xp*cos(Ry) + z1*sin(Ry)
    z2 = -xp*sin(Ry) + z1*cos(Ry)
    x3 = x2*cos(Rz) - y1*sin(Rz)
    y3 = x2*sin(Rz) + y1*cos(Rz)
    return x3, y3, z2

def draw_no_hlr(ax, Rx, Ry, Rz):
    ax.clear()
    coords = [rotate(x[i], y[i], z[i], Rx, Ry, Rz) for i in range(8)]
    for e in edges:
        x1, y1, z1 = coords[e[0]]
        x2, y2, z2 = coords[e[1]]
        ax.plot([x1, x2], [y1, y2], 'k', lw=2)
    ax.set_title("Tanpa Hidden Line Removal")
    ax.axis("equal")
    ax.axis("off")

def draw_hlr(ax, Rx, Ry, Rz):
    ax.clear()
    coords = [rotate(x[i], y[i], z[i], Rx, Ry, Rz) for i in range(8)]
    for e in edges:
        zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
        if zmean > 0:
            x1, y1, z1 = coords[e[0]]
            x2, y2, z2 = coords[e[1]]
            ax.plot([x1, x2], [y1, y2], 'k', lw=2)
    ax.set_title("Dengan Hidden Line Removal")
    ax.axis("equal")
    ax.axis("off")

plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Perbandingan: Non-HLR vs HLR", fontsize=14)
Rx = Ry = Rz = 0

def draw_scene(Rx, Ry, Rz):
    draw_no_hlr(ax1, Rx, Ry, Rz)
    draw_hlr(ax2, Rx, Ry, Rz)
    fig.canvas.draw_idle()
    plt.pause(0.001)

draw_scene(Rx, Ry, Rz)

print("=== Program Gabungan: Non-HLR vs HLR ===")
print("Masukkan sumbu rotasi (x/y/z), atau q untuk keluar.")

while True:
    sumbu = input("\nSumbu (x/y/z/q): ").lower()
    if sumbu == "q":
        break
    try:
        sudut = radians(float(input("Sudut rotasi (derajat): ")))
    except ValueError:
        continue
    if sumbu == "x":
        Rx += sudut
    elif sumbu == "y":
        Ry += sudut
    elif sumbu == "z":
        Rz += sudut
    draw_scene(Rx, Ry, Rz)

plt.ioff()
plt.show()
