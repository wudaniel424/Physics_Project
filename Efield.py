GlowScript 3.0 VPython

iterator = 0 #iterates between resetting arrows

scene.range = 0.02
k=9e9 #k constant
q=1e-9 # test charge 
s=0.001
Escale=2e-8 # scale arrow size

horizontal_axis = vector(1,0,0) #Horizontal vector, used for calculation of the rotation of the ellipse caused by the dipole



qn=sphere(pos=vector(-s/2,-0.003,0), radius=s/5, color=color.cyan) # test sphere (negative)
qp=sphere(pos=vector(s/2,+ 0.003,0), radius=s/5, color=color.yellow) # test sphere (positive)

arrowList = [] #keeps track of all the arrows in the simulation
chargedParticles = []

def eField():
    center = vector(0,0,0)
    for particle in chargedParticles:
        center += particle.pos
    midpoint = center/len(chargedParticles)
    
    distances = []
    for particle in chargedParticles:
        distances.append((chargedParticles.pos - midpoint).mag)


#def dipoleEField3 (sphere1, sphere2, sphere3, charge1, charge2, charge3, eLineCount):
    
def dipoleEField(sphere1, sphere2, charge1, charge2, eLineCount):
    if (abs(charge1) > abs(charge2)): # this is used to space out arrows in case the charges are not equal in magnitude
        chargeScale = abs(charge1)/abs(charge2)
    else:
        chargeScale = abs(charge2)/abs(charge1)
        
    for i in range(5): # how many sets of arrow are outputted from the dipoles to show e field
        sphereVector = sphere1.pos - sphere2.pos
        horizontal_angle = diff_angle (sphereVector, horizontal_axis) # measures how the orientation of the ellipse caused by the spheres is as an angle to horizontal
    
        midpoint = (sphere1.pos + sphere2.pos) * 1/2
        sphere1.q = charge1
        sphere2.q = charge2
    
        sphere_dist = (sphere1.pos - sphere2.pos).mag # distance between spheres, to adjust magnitude of certain objects
        
        if (sphere_dist < 3 * 10**-3):
            A=sphere_dist * 3 + 0.004 + i  * 2 * 0.001 * chargeScale # major axis of the arrow
        else:
            A=sphere_dist + 0.004 + i  * 2 * 0.001 * chargeScale
    
        B = 0.006 + i * 0.001 * chargeScale # minor axis for arrow ellipse
    
        theta = 0 #angle while rotating within the ellipse
        dtheta = 2*pi/eLineCount # change in angle while rotating around points on the ellipse, based on number of arrows desired
    
        while theta<2*pi: # encompasses the entirety of the ellipse
    
            distance = sqrt(A**2*(cos(theta))**2 + B**2*(sin(theta))**2) # distance from midpoint to a point on the ellipse given a certain angle rotation from the vertical
        
            rotated_angle = theta + horizontal_angle #accounts for the shift in positions of the sphere
        
            so=distance*vector(cos(rotated_angle),sin(rotated_angle),0) + midpoint #origin vector of the e field arrows

            s1p=so-sphere1.pos #e direction from first sphere
            s2p=so-sphere2.pos #e direction from second sphere
        
            E1=k*qp.q*s1p/mag(s1p)**3 #e field from first sphere
            E2=k*qn.q*s2p/mag(s2p)**3 #e field from second sphere
        
            E=E1+E2 # combining the e fields

            Earrow=arrow(pos=so, axis=Escale * E / chargeScale) # higher magnitudal charge scaling between charging, the arrows scale appropriately
            
            arrowList.append(Earrow) #adds arrow object to the list for accounting
            
            theta=theta+dtheta # changing arrows

def move1(evt):
    console.log(evt)
    if evt.id is 'x':
        qn.pos.x= evt.value
    else:
        qn.pos.y=evt.value

def move2(evt):
    console.log(evt)
    if evt.id is 'x':
        qp.pos.x= evt.value
    else:
        qp.pos.y=evt.value

x1slider = slider(bind = move1, max = 0.02, min = -0.02, step = 0.001, value = qn.pos.x, id = 'x')
x1text = wtext(text = "X Position of negative particle")
scene.append_to_caption('\n\n')

y1slider = slider(bind = move1, max = 0.02, min = -0.02, step = 0.001, value = qn.pos.y, id = 'y')
y1text = wtext(text = "Y Position of negative particle")
scene.append_to_caption('\n\n')

x2slider = slider(bind = move2, max = 0.02, min = -0.02, step = 0.001, value = qn.pos.x, id = 'x')
x2text = wtext(text = "X Position of positive particle")
scene.append_to_caption('\n\n')

y2slider = slider(bind = move2, max = 0.02, min = -0.02, step = 0.001, value = qn.pos.y, id = 'y')
y2text = wtext(text = "Y Position of positive particle")


def arrowDeletion(): # deletes arrows in accord to tick speed, so that as particles move their e fields are changing
    for arrow in arrowList:
        arrow.visible = False
        del arrow 

while True:
    rate(100)
    dipoleEField(qp, qn, q, -q, 50)
    if (iterator % 4 == 0):
        arrowDeletion()
        iterator = 0
    iterator+=1

#arrowDeletion()


 

