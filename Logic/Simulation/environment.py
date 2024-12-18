import constants as const

def atmosphericpressure(altitude):
    return const.sealevelpressure * (1 - (const.temperaturelapserate * altitude) / const.sealeveltemperature) ** const.pressuredecay

def airdensity(pressure, temperature):
    return pressure / (const.gasconstant * temperature)

def temperature(altitude):
    return const.sealeveltemperature - const.temperaturelapserate * altitude