"""
HLSPHERE
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

plt.axis([0,150,100,0])
plt.axis('off')
plt.grid(False)

g=[0]*3

xc=80
yc=50
zc=0

rs=40

#=========================================================
def rotx(xc,yc,zc,xp,yp,zp,Rx):
    g[0]=xp+xc
    g[1]=yp*cos(Rx)-zp*sin(Rx)+yc
    g[2]=yp*sin(Rx)+zp*cos(Rx)+zc
    return[g]

def roty(xc,yc,zc,xp,yp,zp,Ry):
    g[0]=xp*cos(Ry)+zp*sin(Ry)+xc
    g[1]=yp+yc
    g[2]=-xp*sin(Ry)+zp*cos(Ry)+zc
    return[g]

def rotz(xc,yc,zc,xp,yp,zp,Rz):
    g[0]=xp*cos(Rz)-yp*sin(Rz)+xc
    g[1]=xp*sin(Rz)+yp*cos(Rz)+yc
    g[2]=zp+zc
    return[g]

#————————————————-longitudes and latitudes
phi1=radians(-90)
phi2=radians(90)
dphi=radians(6)

alpha1=radians(0)
alpha2=radians(360)
dalpha=radians(6)

Rx=radians(45)
Ry=radians(-20)
Rz=radians(40)

for alpha in np.arange(alpha1,alpha2,dalpha):  #———longitudes
    for phi in np.arange(phi1,phi2,dphi):
        xp=rs*cos(phi)*cos(alpha)
        yp=rs*sin(phi)
        zp=-rs*cos(phi)*sin(alpha)
        rotx(xc,yc,zc,xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xc,yc,zc,xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        rotz(xc,yc,zc,xp,yp,zp,Rz)
        xpg=g[0]
        ypg=g[1]
        zpg=g[2]
        nz=zpg-zc
        if phi == phi1:
            xpglast=xpg
            ypglast=ypg
        if nz < 0:
            plt.plot([xpglast,xpg],[ypglast,ypg],linewidth=.5,color='g')
        xpglast=xpg
        ypglast=ypg

for phi in np.arange(phi1,phi2,dphi):  #—————latitudes
    r=rs*cos(phi)
    for alpha in np.arange(alpha1,alpha2+dalpha,dalpha):
        xp=r*cos(alpha)
        yp=rs*sin(phi)
        zp=-rs*cos(phi)*sin(alpha)
        rotx(xc,yc,zc,xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xc,yc,zc,xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        rotz(xc,yc,zc,xp,yp,zp,Rz)
        xpg=g[0]
        ypg=g[1]
        zpg=g[2]
        nz=zpg-zc
        if alpha == alpha1:
            xpglast=xpg
            ypglast=ypg
        if nz < 0:
            plt.plot([xpglast,xpg],[ypglast,ypg],linewidth=.5,color='b')
        xpglast=xpg
        ypglast=ypg

plt.show()

