import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

L=(1,1,1)

def NORM(v):
    l=sqrt(v[0]**2+v[1]**2+v[2]**2)
    return (v[0]/l,v[1]/l,v[2]/l)

def DOT(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def ROTATE(xp,yp,zp,Rx,Ry,Rz):
    y1=yp*cos(Rx)-zp*sin(Rx)
    z1=yp*sin(Rx)+zp*cos(Rx)
    x2=xp*cos(Ry)+z1*sin(Ry)
    z2=-xp*sin(Ry)+z1*cos(Ry)
    x3=x2*cos(Rz)-y1*sin(Rz)
    y3=x2*sin(Rz)+y1*cos(Rz)
    return x3,y3,z2

def SHADESPHERE(Rx,Ry,Rz):
    plt.clf()
    plt.axis([-20,20,-20,20])
    plt.axis("off")
    Ln=NORM(L)
    for t in range(0,180,10):
        for p in range(0,360,10):
            x1=10*sin(radians(t))*cos(radians(p))
            y1=10*sin(radians(t))*sin(radians(p))
            z1=10*cos(radians(t))
            n=NORM((x1,y1,z1))
            i=DOT(n,Ln)
            if i<0:i=0
            g=0.2+0.8*i
            c=(g,g,g)
            x2,y2,z2=ROTATE(x1,y1,z1,Rx,Ry,Rz)
            if z2>0:
                plt.scatter(x2,y2,s=15,color=c)
    plt.pause(0.001)

plt.ion()
Rx=Ry=Rz=0
SHADESPHERE(Rx,Ry,Rz)
while True:
    s=input("Sumbu (x/y/z/q): ")
    if s=='q':break
    a=radians(float(input("Sudut: ")))
    if s=='x':Rx+=a
    if s=='y':Ry+=a
    if s=='z':Rz+=a
    SHADESPHERE(Rx,Ry,Rz)
plt.ioff()
plt.show()
