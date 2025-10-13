"""
HLBOX - Hidden Line Box
Program untuk menampilkan kotak 3D dengan penghilangan garis tersembunyi
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

# ============================================
# SETUP PLOTTING AREA
# ============================================
plt.axis([0, 150, 100, 0])
plt.axis('on')
plt.grid(True)

# ============================================
# DEFINISI KOORDINAT KOTAK
# ============================================
# Koordinat 8 sudut kotak (lokal, relatif terhadap pusat)
x = [-20, 20, 20, -20, -20, 20, 20, -20]  # koordinat x
y = [-10, -10, -10, -10, 10, 10, 10, 10]  # koordinat y
z = [5, 5, -5, -5, 5, 5, -5, -5]          # koordinat z

# List untuk koordinat global (hasil rotasi)
xg = [0] * len(x)
yg = [0] * len(x)
zg = [0] * len(x)

# ============================================
# FUNGSI ROTASI
# ============================================

def rotx(xc, yc, zc, xp, yp, zp, Rx):
    """Rotasi titik terhadap sumbu X"""
    xpp = xp
    ypp = yp * cos(Rx) - zp * sin(Rx)
    zpp = yp * sin(Rx) + zp * cos(Rx)
    xg = xpp + xc
    yg = ypp + yc
    zg = zpp + zc
    return [xg, yg, zg]

def roty(xc, yc, zc, xp, yp, zp, Ry):
    """Rotasi titik terhadap sumbu Y"""
    xpp = xp * cos(Ry) + zp * sin(Ry)
    ypp = yp
    zpp = -xp * sin(Ry) + zp * cos(Ry)
    xg = xpp + xc
    yg = ypp + yc
    zg = zpp + zc
    return [xg, yg, zg]

def rotz(xc, yc, zc, xp, yp, zp, Rz):
    """Rotasi titik terhadap sumbu Z"""
    xpp = xp * cos(Rz) - yp * sin(Rz)
    ypp = xp * sin(Rz) + yp * cos(Rz)
    zpp = zp
    xg = xpp + xc
    yg = ypp + yc
    zg = zpp + zc
    return [xg, yg, zg]

# ============================================
# FUNGSI PLOTTING KOTAK DENGAN HIDDEN LINE REMOVAL
# ============================================

def plotbox(xg, yg, zg):
    """
    Menggambar kotak dengan hidden line removal
    Hanya menggambar bidang yang menghadap pengamat
    """
    
    # --- BIDANG 0,1,2,3 (atas) vs BIDANG 4,5,6,7 (bawah) ---
    # Hitung vektor normal bidang menggunakan cross product
    v01x = x[1] - x[0]
    v01y = y[1] - y[0]
    v01z = z[1] - z[0]
    
    v03x = x[3] - x[0]
    v03y = y[3] - y[0]
    v03z = z[3] - z[0]
    
    # Komponen z dari vektor normal (menentukan arah bidang)
    nz = v03x * v01y - v03y * v01x
    
    # Jika nz <= 0, bidang menghadap pengamat (visible)
    if nz <= 0:
        plt.plot([xg[0], xg[1]], [yg[0], yg[1]], color='k', linewidth=2)
        plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k', linewidth=2)
        plt.plot([xg[2], xg[3]], [yg[2], yg[3]], color='k', linewidth=2)
        plt.plot([xg[3], xg[0]], [yg[3], yg[0]], color='k', linewidth=2)
    else:
        plt.plot([xg[4], xg[5]], [yg[4], yg[5]], color='k', linewidth=2)
        plt.plot([xg[5], xg[6]], [yg[5], yg[6]], color='k', linewidth=2)
        plt.plot([xg[6], xg[7]], [yg[6], yg[7]], color='k', linewidth=2)
        plt.plot([xg[7], xg[4]], [yg[7], yg[4]], color='k', linewidth=2)
    
    # --- BIDANG 0,3,7,4 (kiri) vs BIDANG 1,2,6,5 (kanan) ---
    v04x = x[4] - x[0]
    v04y = y[4] - y[0]
    v04z = z[4] - z[0]
    
    v03x = x[3] - x[0]
    v03y = y[3] - y[0]
    v03z = z[3] - z[0]
    
    nz = v04x * v03y - v04y * v03x
    
    if nz <= 0:
        # Gambar bidang kiri (0,3,7,4)
        plt.plot([xg[0], xg[3]], [yg[0], yg[3]], color='k', linewidth=2)
        plt.plot([xg[3], xg[7]], [yg[3], yg[7]], color='k', linewidth=2)
        plt.plot([xg[7], xg[4]], [yg[7], yg[4]], color='k', linewidth=2)
        plt.plot([xg[4], xg[0]], [yg[4], yg[0]], color='k', linewidth=2)
    else:
        # Gambar bidang kanan (1,2,6,5)
        plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k', linewidth=2)
        plt.plot([xg[2], xg[6]], [yg[2], yg[6]], color='k', linewidth=2)
        plt.plot([xg[6], xg[5]], [yg[6], yg[5]], color='k', linewidth=2)
        plt.plot([xg[5], xg[1]], [yg[5], yg[1]], color='k', linewidth=2)
    
    # --- BIDANG 0,1,5,4 (depan) vs BIDANG 3,2,6,7 (belakang) ---
    v01x = x[1] - x[0]
    v01y = y[1] - y[0]
    v01z = z[1] - z[0]
    
    v04x = x[4] - x[0]
    v04y = y[4] - y[0]
    v04z = z[4] - z[0]
    
    nz = v01x * v04y - v01y * v04x
    
    if nz <= 0:
        # Gambar bidang depan (0,1,5,4)
        plt.plot([xg[0], xg[1]], [yg[0], yg[1]], color='k', linewidth=2)
        plt.plot([xg[1], xg[5]], [yg[1], yg[5]], color='k', linewidth=2)
        plt.plot([xg[5], xg[4]], [yg[5], yg[4]], color='k', linewidth=2)
        plt.plot([xg[4], xg[0]], [yg[4], yg[0]], color='k', linewidth=2)
    else:
        # Gambar bidang belakang (3,2,6,7)
        plt.plot([xg[3], xg[2]], [yg[3], yg[2]], color='k', linewidth=2)
        plt.plot([xg[2], xg[6]], [yg[2], yg[6]], color='k', linewidth=2)
        plt.plot([xg[6], xg[7]], [yg[6], yg[7]], color='k', linewidth=2)
        plt.plot([xg[7], xg[3]], [yg[7], yg[3]], color='k', linewidth=2)
    
    # Gambar titik di pusat rotasi
    plt.scatter(xc, yc, s=5, color='k')
    
    # Setup ulang axes dan grid
    plt.axis([0, 150, 100, 0])
    plt.axis('on')
    plt.grid(True)
    plt.show()

# ============================================
# FUNGSI TRANSFORMASI DAN PLOTTING
# ============================================

def plotboxx(xc, yc, zc, Rx):
    for i in range(len(x)):
        [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], Rx)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotbox(xg, yg, zg)

def plotboxy(xc, yc, zc, Ry):
    """Transform dan plot rotasi terhadap sumbu Y"""
    for i in range(len(x)):
        [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], Ry)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotbox(xg, yg, zg)

def plotboxz(xc, yc, zc, Rz):
    """Transform dan plot rotasi terhadap sumbu Z"""
    for i in range(len(x)):
        [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], Rz)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotbox(xg, yg, zg)

# ============================================
# KONTROL PROGRAM - INPUT DARI KEYBOARD
# ============================================

# Koordinat pusat rotasi
xc = 75
yc = 50
zc = 50

# Loop input keyboard
while True:
    axis = input('Rotasi sumbu (x, y, atau z)?: ')
    
    if axis == 'x':
        Rx = radians(float(input('Sudut Rx (derajat)?: ')))
        plotboxx(xc, yc, zc, Rx)
    
    elif axis == 'y':
        Ry = radians(float(input('Sudut Ry (derajat)?: ')))
        plotboxy(xc, yc, zc, Ry)
    
    elif axis == 'z':
        Rz = radians(float(input('Sudut Rz (derajat)?: ')))
        plotboxz(xc, yc, zc, Rz)
    elif axis == 'q':
        break  # Keluar dari program