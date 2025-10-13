"""
Hidden Line Removal - Visualisasi 3D
Menampilkan objek depan (plane miring) dan titik-titik objek belakang (grid)
• Titik hitam  = terlihat oleh pengamat
• Titik merah  = tersembunyi oleh objek depan
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ray_triangle_intersect(orig, dir, v0, v1, v2, eps=1e-9):
    # Algoritma Möller–Trumbore untuk perpotongan ray-triangle
    edge1 = v1 - v0
    edge2 = v2 - v0
    pvec = np.cross(dir, edge2)
    det = np.dot(edge1, pvec)
    if abs(det) < eps:
        return False, None
    inv_det = 1.0 / det
    tvec = orig - v0
    u = np.dot(tvec, pvec) * inv_det
    if u < 0.0 or u > 1.0:
        return False, None
    qvec = np.cross(tvec, edge1)
    v = np.dot(dir, qvec) * inv_det
    if v < 0.0 or u + v > 1.0:
        return False, None
    t = np.dot(edge2, qvec) * inv_det
    if t < eps:
        return False, None
    return True, t

# Objek depan (plane miring)
front_quad = np.array([
    [-20, -10, 8.0],   # A
    [ 40, -10, 9.0],   # B
    [ 30,  20, 12.0],  # C
    [-10,  25, 11.0]   # D
])
front_tris = [
    (front_quad[0], front_quad[1], front_quad[2]),
    (front_quad[0], front_quad[2], front_quad[3])
]

# Objek belakang: grid titik di z = 20
xs = np.linspace(-30, 50, 40)
ys = np.linspace(-25, 30, 35)
xx, yy = np.meshgrid(xs, ys)
zz = np.full(xx.shape, 20.0)
points_back = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T

ray_dir = np.array([0.0, 0.0, -1.0])  # arah ray ke pengamat
visible_pts = []
hidden_pts = []

for p in points_back:
    hit_any = False
    for v0, v1, v2 in front_tris:
        hit, t = ray_triangle_intersect(p, ray_dir, v0, v1, v2)
        if hit:
            hit_any = True
            break
    if hit_any:
        hidden_pts.append(p)
    else:
        visible_pts.append(p)

visible_pts = np.array(visible_pts)
hidden_pts = np.array(hidden_pts)

# Plot 3D
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Simulasi Hidden Line Removal (Tampilan 3D)", fontsize=11)
ax.set_xlabel("X")
ax.set_ylabel("Y")  
ax.set_zlabel("Z")
ax.view_init(elev=25, azim=-60)

# Plot titik belakang (terlihat & tersembunyi)
if visible_pts.size:
    ax.scatter(visible_pts[:,0], visible_pts[:,1], visible_pts[:,2],
               color='k', s=10, label="Titik terlihat (back)")
if hidden_pts.size:
    ax.scatter(hidden_pts[:,0], hidden_pts[:,1], hidden_pts[:,2],
               color='r', s=10, label="Titik tersembunyi (back)")

# Plot bidang depan
quad = np.vstack([front_quad, front_quad[0]])  # tutup loop
ax.plot(quad[:,0], quad[:,1], quad[:,2], '-b', linewidth=2, label="Objek depan")

ax.legend()
plt.tight_layout()
plt.show()
