GlowScript 3.0 VPython


k=9e9
q=1e-9
s=0.001

qn=sphere(pos=vector(-s/2,0,0), radius=s/5, color=color.cyan)
qp=sphere(pos=vector(s/2,0.0025,0), radius=s/5, color=color.yellow)

horizontal_axis = vector(1,0,0)
qpqnvector = qp.pos - qn.pos

horizontal_angle = diff_angle(qpqnvector, horizontal_axis)
print(horizontal_angle)

midpoint = (qn.pos + qp.pos) * 1/2
qn.q=-q
qp.q=q

sphere_dist = (qn.pos-qp.pos).mag

print(sphere_dist)

A=sphere_dist * 2 + 0.002 # major axes of the initial ellipse

B=0.006 # minor
theta=0


N=20
dtheta=2*pi/N
Escale=3e-8

while theta<2*pi:
    
    distance = sqrt(A**2*(cos(theta))**2 + B**2*(sin(theta))**2)
    
    ro=distance*vector(cos(theta+horizontal_angle),sin(theta+horizontal_angle),0) + midpoint

    rp=ro-qp.pos
    rn=ro-qn.pos
    Ep=k*qp.q*rp/mag(rp)**3

    En=k*qn.q*rn/mag(rn)**3
    E=Ep+En

    Earrow=arrow(pos=ro, axis=Escale*  E)
    theta=theta+dtheta




 

