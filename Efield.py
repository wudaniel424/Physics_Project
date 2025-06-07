GlowScript 3.0 VPython
k=9e9
q=1e-9
s=0.001

qn=sphere(pos=vector(-s/2,0,0), radius=s/5, color=color.cyan)
qp=sphere(pos=vector(s/2,0,0), radius=s/5, color=color.yellow)

midpoint = (qn.pos + qp.pos) * 1/2
qn.q=-q
qp.q=q

R=0.006
theta=0


N=16
dtheta=2*pi/N
Escale=3e-8

while R<0.01:
    
    while theta<2*pi:
  
        ro=R*vector(cos(theta),sin(theta),0) - midpoint

        rp=ro-qp.pos
        rn=ro-qn.pos
        Ep=k*qp.q*rp/mag(rp)**3

        En=k*qn.q*rn/mag(rn)**3
        E=Ep+En

        Earrow=arrow(pos=ro, axis=Escale*E)
        theta=theta+dtheta

    theta=0
    R+=0.001


 

