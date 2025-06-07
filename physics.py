Web VPython 3.2
#hi ms sharaf this is a bit of a mess right now im doing some testing without user inputs on another glowscript doc and put that code in here, will fix soon
scene = canvas(width = 600, height = 600)

e = 1.6e-19 #elementary charge
k = 9e9 #Coulomb's law constant
dt = 100 #dt value
t = 0 #initial t
cl.charge = -e
h20dipolemoment = 6e-30 #Cm

e=1.6e-19




def efield(particle1, particle2):
    return ((k*particle1.charge/((particle1.pos - particle2.pos).mag)**2))*hat(particle1.pos - particle2.pos)
def force(particle1, particle2):
    return (particle2.charge*efield(particle1,particle2))
def dipolemoment(particle, positivecharge,negativecharge):
    return particle.charge*(postivecharge.pos - negativecharge.pos)
def torque(moment, field, theta):
    return cross(moment,field)
    
    
    

def cl(x,y):
    return sphere(pos = vector(x,y,0), radius = 79, color = color.green)
def h2o(x,y):
    oxy = sphere(pos = vector(x,y,0), radius = 48, color = color.red)
    hydro1 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y+95.84*sin(radians(52.225)),0), radius = 37)
    hydro2 = sphere(pos = vector(x+95.84*cos(radians(52.225)),y-95.84*sin(radians(52.225)),0), radius = 37)
    h2o = compoud([oxy, hydro1, hydro2])
    h2o(pos = vector(x,y,0))
def xpos(evt):
    return xpos = evt.value
def ypos(evt):
    return ypos = evt.value

xposslider = slider(bind = xpos, min = 0, max = 1000, step = 1)
wtx = wtext(text='0')
yposslider = slider(bind = ypos, min = 0, max = 1000, step = 1)
wty = wtext(text='0')



def part1(evt):
    if evt.text is 'chlorine':
        part1 = cl(0,0,0)
        part1.charge = e
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

        oxy.charge = -0.358*e
        oxy.pos = vector(0,0,0)
        oxy.velocity = vec(0,0,0)
        oxy.acceleration = vec(0,0,0)
        oxy.mass = 2.6566962e-26
        
        h2ocom = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
        h2o.origin = h2ocom

def part2(evt):
    if evt.text is 'chlorine':
        part2 = cl(xposslider.value,yposslider.value)
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

        oxy.charge = -0.358*e
        oxy.pos = vector(xposslider.value,yposslider.value,0)
        oxy.velocity = vec(0,0,0)
        oxy.acceleration = vec(0,0,0)
        oxy.mass = 2.6566962e-26
        
        h2ocom = (hydro1.mass*hydro1.pos + hydro2.mass*hydro2.pos + oxy.mass*oxy.pos)/(hydro1.mass+hydro2.mass+oxy.mass)
        h2o.origin = h2ocom


chlorine = radio(bind=part1,text='chlorine', name='part1')
water = radio(bind=part1, text='water', name='part1')

chlorine2 = radio(bind=part2,text='chlorine', name='part2')
water2 = radio(bind=part2, text='water', name='part2')

#if 
while True:
    rate(100)
    
    
    
    wtx.text = "X position (pm) = "'{:.2f}'.format(xposslider.value)
    wty.text = "Y position (pm) = " '{:.2f}'.format(yposslider.value)
    t+dt


