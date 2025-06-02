Web VPython 3.2

scene = canvas(width = 600, height = 600)

e = 1.6e-19 #elementary charge
k = 9e9 #Coulomb's law constant
dt = 1000
t = 0



def dipolemoment(particle, positivecharge,negativecharge):
    return particle.charge*(postivecharge.pos - negativecharge.pos)
def torque(moment, field, theta):
    return cross(moment,field)
def force(particle1, particle2):
    return (k*particle1.charge*particle2.charge)/(((particle1.pos-particle2.pos).mag)**2)
    
    
    

def cl(x,y,z):
    cl.charge = -e
    return sphere(pos = vector(x,y,z), radius = 79, color = color.green)
def h2o(x,y,z):
    oxy = sphere(pos = vector(x,y,z), radius = 48, color = color.red)
    hydro1 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y+95.84*sin(radians(52.225)),z), radius = 37)
    hydro2 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y-95.84*sin(radians(52.225)),z), radius = 37)
    h20 = compoud([oxy, hydro1, hydro2])
    hydro1.charge 
    return h2o(pos = vector (x,y,z))
def xpos(evt):
    return xpos = evt.value
def ypos(evt):
    return ypos = evt.value
def zpos(evt):
    return zpos = evt.value

xposslider = slider(bind = xpos, min = 1, max = 1000, step = 1)
yposslider = slider(bind = ypos, min = 1, max = 1000, step = 1)
zposslider = slider(bind = zpos, min = 1, max = 1000, step = 1)

def part1(evt):
    if evt.text is 'chlorine':
        part1 = cl(0,0,0)
    elif evt.text is 'water':
        part1 = h2o(0,0,0)

def part2(evt):
    if evt.text is 'chlorine':
        part2 = cl(xpos,ypos,zpos)
    elif evt.text is 'water':
        part2 = h2o(xpos,ypos,zpos)
    


chlorine = radio(bind=part1,text='chlorine', name='part1')
water = radio(bind=part1, text='water', name='part1')

chlorine2 = radio(bind=part2,text='chlorine', name='part2')
water2 = radio(bind=part2, text='water', name='part2')

permittivity = 8.85e-12 

def fieldmag(particle):
    rad = (particle.pos - point.pos)
    return ((1/(4*pi*permittivity*rad**2))*particle.charge)
    
while((part2.pos-part2.pos).mag>(part1.radius+part2.radius)):
    rate(dt)
    a = force(part1,part2)
    v = a*dt
    x = v*dt
    part1.pos = part1.pos
    t = t+dt

