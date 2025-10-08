import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

# Titik-titik kubus
x = [-10, 10, 10, -10, -10, 10, 10, -10]
y = [-10, -10, 10, 10, -10, -10, 10, 10]
z = [10, 10, 10, 10, -10, -10, -10, -10]

# Setiap sisi kubus terdiri dari 4 titik (urutan vertex)
faces = [
    [0, 1, 2, 3],  # depan
    [4, 5, 6, 7],  # belakang
    [0, 1, 5, 4],  # bawah
    [2, 3, 7, 6],  # atas
    [1, 2, 6, 5],  # kanan
    [0, 3, 7, 4]   # kiri
]

# Arah cahaya (misalnya datang dari depan-kanan-atas)
light_dir = (1, 1, 1)

def normalize(v):
    l = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return (v[0]/l, v[1]/l, v[2]/l)

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

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
    plt.axis([0, 150, 100, 0])
    plt.axis("off")
    plt.title("Chapter 7 – SHADEBOX")

    xc, yc = 75, 50
    coords = [rotate(x[i], y[i], z[i], Rx, Ry, Rz) for i in range(8)]
    light = normalize(light_dir)

    for f in faces:
        p1, p2, p3, p4 = [coords[i] for i in f]
        # Hitung vektor normal permukaan
        ux, uy, uz = p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]
        vx, vy, vz = p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]
        nx = uy*vz - uz*vy
        ny = uz*vx - ux*vz
        nz = ux*vy - uy*vx
        n = normalize((nx, ny, nz))

        intensity = dot(n, light)
        if intensity < 0: intensity = 0  # permukaan membelakangi cahaya

        gray = 0.2 + 0.8 * intensity  # kecerahan
        color = (gray, gray, gray)    # warna abu-abu berdasarkan intensitas

        # Jika permukaan menghadap ke depan, gambar
        zmean = (p1[2]+p2[2]+p3[2]+p4[2])/4
        if zmean > 0:
            plt.fill([xc+p1[0], xc+p2[0], xc+p3[0], xc+p4[0]],
                     [yc-p1[1], yc-p2[1], yc-p3[1], yc-p4[1]],
                     color=color, edgecolor='k')

    plt.pause(0.001)

plt.ion()
Rx = radians(25)
Ry = radians(30)
Rz = 0
draw_box(Rx, Ry, Rz)

print("=== SHADEBOX ===")
print("Masukkan sumbu rotasi (x/y/z), q untuk keluar.")
while True:
    s = input("\nSumbu (x/y/z/q): ").lower()
    if s == "q": break
    try:
        a = radians(float(input("Sudut rotasi (°): ")))
    except ValueError:
        continue
    if s == "x": Rx += a
    elif s == "y": Ry += a
    elif s == "z": Rz += a
    draw_box(Rx, Ry, Rz)
plt.ioff()
plt.show()