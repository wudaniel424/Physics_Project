Web VPython 3.2
scene = canvas(width = 600, height = 600)

e = 1.6e-19 #elementary charge
k = 9e9 #Coulomb's law constant
dt = 100 #dt value
t = 0 #initial t

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

xposslider = slider(bind = xpos, min = 79, max = 1000, step = 1)
wtx = wtext(text='0')
yposslider = slider(bind = ypos, min = 79, max = 1000, step = 1)
wty = wtext(text='0')

part1 = cl(0,0,0)
generate = False

def genPart2(evt):
    global generate
    if evt.text == 'Generate Second Particle':
        generate = True
generateButton = button(bind = genPart2, text = 'Generate Second Particle')

Particle2 ='placeholder'
def particle2Choose(evt):
    global Particle2
    if evt.text is 'Chlorine':
        Particle2 = 'Chlorine'
    elif evt.text is 'Water':
        Particle2 = 'Water'   
chlorine = radio(bind=particle2Choose,text='Chlorine', name='part2', pos = scene.append_to_caption('\n\n\n'))
water = radio(bind=particle2Choose, text='Water', name='part2',pos = scene.append_to_caption('\n\n\n'))

run = False
def runSimulation(evt):
    global run
    if evt.text == 'Run Simulation':
        run = True      
runButton = button(bind = runSimulation, text = 'Run Simulation')

while True:
    rate(100)
    if generate == True:
        if Particle2 == 'Water':
            part2 = h2o(xposslider.value, yposslider.value)
            oxy = sphere(pos = vector(xposslider.value, yposslider.value, 0), radius = 48, color = color.red)
            hydro1 = sphere(pos = vector(xposslider.value + 95.84 * cos(radians(52.225)),yposslider.value + 95.84 * sin(radians(52.225)), 0), radius = 37)
            hydro2 = sphere(pos = vector(xposslider.value + 95.84 * cos(radians(52.225)),yposslider.value - 95.84 * sin(radians(52.225)), 0), radius = 37)
            
            hydro1.pos = vector(xposslider.value+95.84*cos(radians(52.225)),yposslider.value+95.84*sin(radians(52.225)),0)
            hydro1.mass = 1.6735575e-27
            hydro2.pos = vector(xposslider.value+95.84*cos(radians(52.225)),yposslider.value-95.84*sin(radians(52.225)),0)
            hydro2.mass = 1.6735575e-27
            oxy.pos = vector(xposslider.value,yposslider.value,0)
            oxy.mass = 2.6566962e-26
        
            part2.com = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
            #part2.origin = h2o.com
            part2.inertia = hydro1.mass*(hydro1.pos - h2o.com).mag**2+hydro2.mass*(hydro2.pos - h2o.com).mag**2+oxy.mass*(oxy.pos - h2o.com).mag**2
            part2.moment = 6e-18*(oxy.pos - h2o.com) #C*pm
            part2.torque = 0
            part2.angAcc = 0
            part2.angVel = 0
            part2.angDisp = 0
            print(part2.inertia)
        elif Particle2 == 'Chlorine':
            part2 = cl(xposslider.value, yposslider.value)
            part2.charge = -e
    if run == True:
        part1.pos = part1.pos + vector(100, 0, 0)  # example update, make sure part1 is defined
        part2torque = cross(part2.moment, efield(part1, part2))
        part2angAcc = part2.torque/part2.inertia
        part2angVel = part2.angVel + part2.angAcc * dt
        part2angDisp = part2.angVel * dt
        rotate(part2, axis=vector(0, 0, 1), angle=part2angDisp, origin=part2com)
    wtx.text = "X position (pm) = " + '{:.2f}'.format(xposslider.value)
    wty.text = "Y position (pm) = " + '{:.2f}'.format(yposslider.value)
