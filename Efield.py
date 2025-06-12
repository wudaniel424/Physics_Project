GlowScript 3.0 VPython



k=9e9
q=1e-9
s=0.001
Escale=2e-8

horizontal_axis = vector(1,0,0) #Horizontal

qn=sphere(pos=vector(-s/2,-0.003,0), radius=s/5, color=color.cyan)
qp=sphere(pos=vector(s/2,+0.003,0), radius=s/5, color=color.yellow)

def dipoleEField(sphere1, sphere2, charge1, charge2, eLineCount):
    for i in range(5):
        sphereVector = sphere1.pos - sphere2.pos
        horizontal_angle = diff_angle (sphereVector, horizontal_axis)
    
        midpoint = (sphere1.pos + sphere2.pos) * 1/2
        sphere1.q = charge1
        sphere2.q = charge2
    
        sphere_dist = (sphere1.pos - sphere2.pos).mag
        print(sphere_dist)
        if (sphere_dist < 3 * 10**-3):
            A=sphere_dist * 3 + 0.004 # major axes of the initial ellipse
        else:
            A=sphere_dist + 0.004
    
        B = 0.006
    
        theta = 0
        dtheta = 2*pi/eLineCount
    
        while theta<2*pi:
    
            distance = sqrt(A**2*(cos(theta))**2 + B**2*(sin(theta))**2)
        
            rotated_angle = theta + horizontal_angle#accounts for the shift in positions of the sphere
        
            so=distance*vector(cos(rotated_angle),sin(rotated_angle),0) + midpoint #origin vector of the e field arrows

            s1p=so-sphere1.pos #e direction from first sphere
            s2p=so-sphere2.pos #e direction from second sphere
        
            E1=k*qp.q*s1p/mag(s1p)**3 #e field from first sphere
            E2=k*qn.q*s2p/mag(s2p)**3 #e field from second sphere
        
            E=E1+E2 # combining the e fields

            Earrow=arrow(pos=so, axis=Escale * E)
            theta=theta+dtheta


dipoleEField(qp, qn, q, -q, 50)
