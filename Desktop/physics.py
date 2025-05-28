Web VPython 3.2

scene = canvas(width = 600, height = 600)



def cl():
    return sphere(pos = vector(0,0,0), radius = 2)
def h2o():
    return sphere(pos = vector (100,100,0), radius = 3)

def part1(evt):
    if evt.text is 'chlorine':
        cl
    elif evt.text is 'water':
        water
    


chlorine = radio(bind=part1,text='chlorine')
water = radio(bind=part1, text='water')


permittivity = 8.85e-12
def fieldmag(particle):
    rad = (particle.pos - point.pos)
    return ((1/(4*pi*permittivity*rad**2))*particle.charge)

