import matplotlib.pyplot as plt
from math import sin, cos, radians

x=[-10,10,10,-10,-10,10,10,-10]
y=[-10,-10,10,10,-10,-10,10,10]
z=[10,10,10,10,-10,-10,-10,-10]

edge=[[0,1],[1,2],[2,3],[3,0],
      [4,5],[5,6],[6,7],[7,4],
      [0,4],[1,5],[2,6],[3,7]]

def ROTATE(xp,yp,zp,Rx,Ry,Rz):
    y1=yp*cos(Rx)-zp*sin(Rx)
    z1=yp*sin(Rx)+zp*cos(Rx)
    x2=xp*cos(Ry)+z1*sin(Ry)
    z2=-xp*sin(Ry)+z1*cos(Ry)
    x3=x2*cos(Rz)-y1*sin(Rz)
    y3=x2*sin(Rz)+y1*cos(Rz)
    return x3,y3,z2

def PLOTBOX(Rx,Ry,Rz):
    plt.clf()
    plt.axis([-20,20,-20,20])
    plt.axis("off")
    for e in edge:
        a,b=e
        p1=ROTATE(x[a],y[a],z[a],Rx,Ry,Rz)
        p2=ROTATE(x[b],y[b],z[b],Rx,Ry,Rz)
        zm=(p1[2]+p2[2])/2
        if zm>0: plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'k')
    plt.pause(0.001)

plt.ion()
Rx=Ry=Rz=0
PLOTBOX(Rx,Ry,Rz)
while True:
    s=input("Sumbu (x/y/z/q): ")
    if s=='q':break
    a=radians(float(input("Sudut: ")))
    if s=='x':Rx+=a
    if s=='y':Ry+=a
    if s=='z':Rz+=a
    PLOTBOX(Rx,Ry,Rz)
plt.ioff()
plt.show()
