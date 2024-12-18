import constants as const

def dragcoefficient(speed, altitude):
    return const.dragcoefficientbaseline + const.dragspeedfactor * speed + const.altitudefactor * altitude

def liftcoefficient(speed, altitude):
    return const.liftcoefficientbaseline - const.liftspeedfactor * speed - const.altitudefactor * altitude

def drag(wingarea, speed, density, altitude):
    return 0.5 * density * dragcoefficient(speed, altitude) * wingarea * (speed ** 2)

def lift(wingarea, speed, density, altitude):
    return 0.5 * density * liftcoefficient(speed, altitude) * wingarea * (speed ** 2)