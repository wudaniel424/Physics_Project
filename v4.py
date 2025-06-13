Web VPython 3.2
scene = canvas(width = 600, height = 600)

e = 1.6e-19 #elementary charge
k = 9e9 #Coulomb's law constant
dt = 100 #dt value
t = 0 #initial t
horizontal_axis = vector(1,0,0) #Horizontal vector, used for calculation of the rotation of the ellipse caused by the dipole
negative_axis = vector(-1,0,0)

vertical_axis = vector(0,1,0)
negative_vertical = vector(0,-1,0)
def efield(particle1, particle2):
    return ((k*particle1.charge/((particle1.pos - particle2.pos).mag)**2))*(particle2.pos - particle1.pos).hat


def cl(x,y):
    return sphere(pos = vector(x,y,0), radius = 79, color = color.green)
def h2o(x,y):
    oxy = sphere(pos = vector(x, y, 0), radius = 48, color = color.red)
    hydro1 = sphere(pos = vector(x + 95.84 * cos(radians(52.225)),y + 95.84 * sin(radians(52.225)), 0), radius = 37)
    hydro2 = sphere(pos = vector(x + 95.84 * cos(radians(52.225)),y - 95.84 * sin(radians(52.225)), 0), radius = 37)
    return compound([oxy, hydro1, hydro2])

def xpos(evt):
    return xpos = evt.value
def ypos(evt):
    return ypos = evt.value
def rotAngle(evt):
    return rotAngle = evt.value

xposslider = slider(bind = xpos, min = 79, max = 1000, step = 1)
wtx = wtext(text='0')
yposslider = slider(bind = ypos, min = 79, max = 1000, step = 1)
wty = wtext(text='0')
#rotAngleSlider = slider(bind = rotAngle, min = 0, max = 2*pi, step = 0.1)
#wtAngle = wtext(text = '0')

part1 = cl(0,0,0)
part1.charge = -e
generate = False

def genPart2(evt):
    global generate
    if evt.text == 'Generate Second Particle':
        generate = True
        generateButton.delete()
generateButton = button(bind = genPart2, text = 'Generate Second Particle',pos = scene.append_to_caption('\n'))

Particle2 ='placeholder'
def particle2Choose(evt):
    global Particle2
    if evt.text is 'Chlorine':
        Particle2 = 'Chlorine'
    elif evt.text is 'Water':
        Particle2 = 'Water'   

run = False
def runSimulation(evt):
    global run
    if evt.text == 'Run Simulation':
        run = True      
runButton = button(bind = runSimulation, text = 'Run Simulation')

arrowShow = False
def arrowShowFxn(evt):
    global arrowShow
    if evt.text == 'Show Dipole Arrow':
        arrowShow = True
        dipoleArrow.visible = True
        arrowShowButton.text = 'Hide Dipole Arrow'
    elif evt.text == 'Hide Dipole Arrow':
        arrowShow = False
        dipoleArrow.visible = False
        arrowShowButton.text = 'Show Dipole Arrow'
arrowShowButton = button(bind = arrowShowFxn, text = 'Show Dipole Arrow')

def Rz(ve, angle):
    newx = cos(angle)*ve.x - sin(angle)*ve.y
    newy = sin(angle)*ve.x + cos(angle)*ve.y
    return vector(newx,newy,ve.z)

dipoleVisualization = False
def dipoleVisualizationFxn(evt):
    global dipoleVisualization
    if evt.text == 'Enter Dipole Electric Field Visualization Mode':
        dipoleVisualization = True
dipoleVisualizationButton = button(bind = dipoleVisualizationFxn, text = 'Enter Dipole Electric Field Visualization Mode')

chlorine = radio(bind=particle2Choose,text='Chlorine', name='part2', pos = scene.append_to_caption('\n\n\n'))
water = radio(bind=particle2Choose, text='Water', name='part2',pos = scene.append_to_caption('\n\n\n'))
#torqueGraph = graph(title = 'Torque vs. Angle'

while True:
    rate(2000)
    if generate == True:
        if Particle2 == 'Water':
            part2 = h2o(xposslider.value, yposslider.value)
            oxy = sphere(pos = vector(xposslider.value, yposslider.value, 0), radius = 48, color = color.red, visible = False)
            hydro1 = sphere(pos = vector(xposslider.value + 95.84 * cos(radians(52.225)),yposslider.value + 95.84 * sin(radians(52.225)), 0), radius = 37, visible = False)
            hydro2 = sphere(pos = vector(xposslider.value + 95.84 * cos(radians(52.225)),yposslider.value - 95.84 * sin(radians(52.225)), 0), radius = 37, visible = False)
            hydro1.mass = 1.6735575e-12#pg
            hydro2.mass = 1.6735575e-12
            oxy.mass = 2.6566962e-11
        
            part2.com = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
            #part2.origin = h2o.com
            part2.inertia = hydro1.mass*(hydro1.pos - part2.com).mag**2+hydro2.mass*(hydro2.pos - part2.com).mag**2+oxy.mass*(oxy.pos - part2.com).mag**2
            part2.moment = 6e-18*(part2.com - oxy.pos).hat #C*pm
            part2.torque = 0
            part2.angAcc = 0
            part2.angVel = 0
            part2.angDisp = 0
            #rotate(part2, axis = vector(0,0,1), angle = rotAngleSlider.value, origin=(xposslider.value,yposslider.value,0))
            generate = False
            print(part2.com)
            dipoleArrow = arrow(pos = part2.com, axis = part2.moment*1e19, visible = False)
        elif Particle2 == 'Chlorine':
            part2 = cl(xposslider.value, yposslider.value)
            part2.charge = -e
            generate = False
    if run == True:
        if ((diff_angle(part2.moment, negative_axis) > diff_angle(efield(part1,part2), negative_axis) and diff_angle(part2.moment, negative_vertical) < diff_angle(efield(part1,part2), negative_vertical)) or (diff_angle(part2.moment, negative_axis) < diff_angle(efield(part1,part2), negative_axis) and diff_angle(part2.moment, negative_vertical) > diff_angle(efield(part1,part2), negative_vertical))):
            part2.torque = (part2.moment).mag*efield(part1,part2).mag*sin(2*pi - diff_angle(part2.moment,efield(part1,part2)))*1e18
            print(sin(2*pi - diff_angle(part2.moment,efield(part1,part2))))
        else:
            part2.torque = (part2.moment).mag*efield(part1,part2).mag*sin(diff_angle(part2.moment,efield(part1,part2)))*1e18
            print(sin(diff_angle(part2.moment,efield(part1,part2))))
        part2.angAcc = part2.torque/part2.inertia
        part2.angVel = part2.angVel + part2.angAcc*dt
        part2.angDisp = part2.angVel*dt
#        if pi<diff_angle(part2.moment,efield(part1,part2))<2*pi:
        #    part2.angDisp = -part2.angDisp
        rotate(part2, axis=vector(0, 0, 1), angle=part2.angDisp, origin=part2.com)
        rotate(dipoleArrow, axis=vector(0,0,1), angle = part2.angDisp, origin=part2.com)
        part2.moment = 6e-18*(dipoleArrow.axis).hat
        #print(diff_angle(part2.moment,efield(part1,part2)))
    if dipoleVisualization == True:
        del part1
        s=0.001
        q=1e-9
        Escale=2e-8 # scale arrow size

        

        qn=sphere(pos=vector(-s/2,-0.003,0), radius=s/5, color=color.cyan) # test sphere (positive)
        qp=sphere(pos=vector(s/2,+ 0.003,0), radius=s/5, color=color.yellow) # test sphere (negative)

        arrowList = [] #keeps track of all the arrows in the simulation

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


        def arrowDeletion(): # deletes arrows in accord to tick speed, so that as particles move their e fields are changing
            for arrow in arrowList:
                arrow.visible = False
                del arrow 
    
        dipoleEField(qp, qn, q, 3 * -q, 50)

        #arrowDeletion()


        
        
    wtx.text = "X position (pm) = " + '{:.2f}'.format(xposslider.value)
    wty.text = "Y position (pm) = " + '{:.2f}'.format(yposslider.value)
    #wtAngle.text = "Initial Angle of Rotation (radians) = " + '{:.2f}'.format(rotAngleSlider.value)
