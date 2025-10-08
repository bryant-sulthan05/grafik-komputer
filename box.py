import matplotlib.pyplot as plt
from math import sin, cos, radians

x = [-10, 10, 10, -10, -10, 10, 10, -10]
y = [-10, -10, 10, 10, -10, -10, 10, 10]
z = [10, 10, 10, 10, -10, -10, -10, -10]

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

def rotate(xp, yp, zp, Rx, Ry, Rz):
    y1 = yp*cos(Rx) - zp*sin(Rx)
    z1 = yp*sin(Rx) + zp*cos(Rx)
    x2 = xp*cos(Ry) + z1*sin(Ry)
    z2 = -xp*sin(Ry) + z1*cos(Ry)
    x3 = x2*cos(Rz) - y1*sin(Rz)
    y3 = x2*sin(Rz) + y1*cos(Rz)
    return x3, y3, z2

def draw_box(Rx, Ry, Rz):
    plt.clf()
    plt.axis([0,150,100,0])   # seperti layout eBook
    plt.axis("off")
    plt.title("Hidden Line Removal – Box (versi eBook)")
    xc, yc = 75, 50           # titik tengah layar
    coords = []
    for i in range(8):
        xp, yp, zp = rotate(x[i], y[i], z[i], Rx, Ry, Rz)
        coords.append((xc+xp, yc-yp, zp))
    for e in edges:
        zmean = (coords[e[0]][2] + coords[e[1]][2]) / 2
        if zmean > 0:
            plt.plot([coords[e[0]][0], coords[e[1]][0]],
                     [coords[e[0]][1], coords[e[1]][1]], 'k', lw=2)
    plt.pause(0.001)

plt.ion()
# sudut awal supaya bentuk 3D terlihat
Rx = radians(25)
Ry = radians(30)
Rz = 0
draw_box(Rx, Ry, Rz)

print("=== HLBOX (Versi eBook) ===")
print("Masukkan sumbu rotasi (x/y/z), q untuk keluar.")
while True:
    s = input("\nSumbu (x/y/z/q): ").lower()
    if s == "q": break
    a = radians(float(input("Sudut rotasi (°): ")))
    if s == "x": Rx += a
    elif s == "y": Ry += a
    elif s == "z": Rz += a
    draw_box(Rx, Ry, Rz)
plt.ioff()
plt.show()
