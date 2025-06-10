Web VPython 3.2
#hi ms sharaf this is a bit of a mess right now im doing some testing without user inputs on another glowscript doc and put that code in here, will fix soon
scene = canvas(width = 600, height = 600)

e = 1.6e-19 #elementary charge
k = 9e9 #Coulomb's law constant
dt = 100 #dt value
t = 0 #initial t
part2com = 0
part2inertia = 0
part2moment = 0
part2torque = 0
part2angAcc = 0
part2angVel = 0
part2angDisp = 0

def cross(a, b):
    return vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)



def efield(particle1, particle2):
    return ((k*particle1.charge/((particle1.pos - particle2.pos).mag)**2))*(particle1.pos - particle2.pos).hat
def force(particle1, particle2):
    return (particle2.charge*efield(particle1,particle2))
#def torque(particle, force)
 #   return (particle.inertia*particle.
    
    
    

def cl(x,y):
    return sphere(pos = vector(x,y,0), radius = 79, color = color.green)
def h2o(x,y):
    oxy = sphere(pos = vector(x,y,0), radius = 48, color = color.red)
    hydro1 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y+95.84*sin(radians(52.225)),0), radius = 37)
    hydro2 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y-95.84*sin(radians(52.225)),0), radius = 37)
    h2o = compound([oxy, hydro1, hydro2])
    h2o(pos = vector(x,y,0))
def xpos(evt):
    return xpos = evt.value
def ypos(evt):
    return ypos = evt.value

xposslider = slider(bind = xpos, min = 0, max = 1000, step = 1)
wtx = wtext(text='0')
yposslider = slider(bind = ypos, min = 0, max = 1000, step = 1)
wty = wtext(text='0')



def particle1(evt):
    global part1
    global part1charge
    if evt.text is 'chlorine':
        part1 = cl(0,0,0)
        part1charge = -e
    elif evt.text is 'water':
        part1 = h2o(0,0,0)
        hydro1.charge = 0.179*e
        hydro1.pos = vector(95.84*cos(radians(52.225)),95.84*sin(radians(52.225)),0)
        hydro1.velocity = vec(0,0,0)
        hydro1.acceleration = vec(0,0,0)
        hydro1.mass = 1.6735575e-27

        hydro2.charge = 0.179*e
        hydro2.pos = vector(95.84*cos(radians(52.225)),-95.84*sin(radians(52.225)),0)
        hydro2.velocity = vec(0,0,0)
        hydro2.acceleration = vec(0,0,0)
        hydro2.mass = 1.6735575e-27

        oxy.charge = 0.358*-e
        oxy.pos = vector(0,0,0)
        oxy.velocity = vec(0,0,0)
        oxy.acceleration = vec(0,0,0)
        oxy.mass = 2.6566962e-26
        
        h2o.com = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
        h2o.origin = h2o.com
        h2o.inertia = hydro1.mass*(hydro1.pos - h2o.com).mag**2+hydro2.mass*(hydro2.pos - h2o.com).mag**2+oxy.mass*(oxy.pos - h2o.com).mag**2

def particle2(evt):
    global part2
    global part2com
    global part2inertia
    global part2moment
    global part2torque
    global part2angAcc
    global part2angVel
    global part2angDisp
    if evt.text is 'chlorine':
        part2 = cl(xposslider.value,yposslider.value)
        cl.charge = -e
    elif evt.text is 'water':
        part2 = h2o(xposslider.value,yposslider.value)
        hydro1.charge = 0.179*e
        hydro1.pos = vector(xposslider.value+95.84*cos(radians(52.225)),yposslider.value+95.84*sin(radians(52.225)),0)
        hydro1.velocity = vec(0,0,0)
        hydro1.acceleration = vec(0,0,0)
        hydro1.mass = 1.6735575e-27

        hydro2.charge = 0.179*e
        hydro2.pos = vector(xposslider.value+95.84*cos(radians(52.225)),yposslider.value-95.84*sin(radians(52.225)),0)
        hydro2.velocity = vec(0,0,0)
        hydro2.acceleration = vec(0,0,0)
        hydro2.mass = 1.6735575e-27

        oxy.charge = 0.358*-e
        oxy.pos = vector(xposslider.value,yposslider.value,0)
        oxy.velocity = vec(0,0,0)
        oxy.acceleration = vec(0,0,0)
        oxy.mass = 2.6566962e-26
        
        part2com = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
        part2.origin = h2o.com
        part2inertia = hydro1.mass*(hydro1.pos - h2o.com).mag**2+hydro2.mass*(hydro2.pos - h2o.com).mag**2+oxy.mass*(oxy.pos - h2o.com).mag**2
        part2moment = 6e-18*(oxy.pos - h2o.com) #C*pm
        part2torque = 0
        part2angAcc = 0
        part2angVel = 0
        part2angDisp = 0



chlorine = radio(bind=particle1,text='chlorine', name='part1', pos = scene.append_to_caption('\n\n'))
water = radio(bind=particle1, text='water', name='part1', pos = scene.append_to_caption('\n\n'))

chlorine2 = radio(bind=particle2,text='chlorine', name='part2', pos = scene.append_to_caption('\n\n\n'))
water2 = radio(bind=particle2, text='water', name='part2',pos = scene.append_to_caption('\n\n\n'))

#arrow(headlength = 10, shaftwidth = 0.1)

run = False

def runSimulation(evt):
    global run
    if evt.text == 'Run Simulation':
        run = True
        
runButton = button(bind = runSimulation, text = 'Run Simulation')

while True:
    rate(100)
    if run == True:
        part1.pos = part1.pos + vector(100, 0, 0)  # example update, make sure part1 is defined
        part2torque = cross(part2moment, vector(100,100,0))
        part2angAcc = part2torque/ part2inertia
        part2angVel = part2angVel + part2angAcc * dt
        part2angDisp = part2angVel * dt
        rotate(part2, axis=vector(0, 0, 1), angle=part2angDisp, origin=part2com)
        t = t + dt
    wtx.text = "X position (pm) = " + '{:.2f}'.format(xposslider.value)
    wty.text = "Y position (pm) = " + '{:.2f}'.format(yposslider.value)


