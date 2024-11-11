#Get the user's name and wieght.
sName=input('What is your name? ')
nWEIGHT=float(input('What is your weight? '))
#Get the weight of user by calculating (earth weight x planets Surface Gravity Factor).
#Calculate weight planets.
nMercury_SGF = 0.38
nVenus_SGF = 0.91
nMoon_SGF = 0.165
nMars_SGF = 0.38
nJupiter_SGF = 2.34
nSaturn_SGF = 0.93
nUranus_SGF = 0.92
nNeptune_SGF = 1.12
nPluto_SGF = 0.066

MERCURY=float(nWEIGHT * 0.38)
VENUS=float(nWEIGHT * 0.91)
MOON=float(nWEIGHT * 0.165)
MARS=float(nWEIGHT * 0.38)
JUPITER=float(nWEIGHT * 2.34)
SATURN=float(nWEIGHT * 0.93)
URANUS=float(nWEIGHT * 0.92)
NEPTUNE=float(nWEIGHT * 1.12)
PLUTO=float(nWEIGHT * 0.066)

#Display planets #Display user's name and the statement ' here are your weights on our Solar System's
#planets:'.
print(sName, 'here is your weights on our Soloar System\'s planets:')
#Display the weights for the corresponding planets.
print('Weight on MERCURY:', format(MERCURY, '10.2f'))            #Mecury weight
print('Weight on Venus:', format(VENUS, '10.2f'))                #Venus weight
print('Weight on Moon:', format(MOON, '10.2f'))                  #Moon weight
print('Weight on Mars:', format(MARS, '10.2f'))                  #Mars weight
print('Weight on Jupiter:', format(JUPITER, '10.2f'))            #Jupiter weight
print('Weight on Saturn:', format(SATURN, '10.2f'))              #Saturn weight
print('Weight on Uranus:', format(URANUS, '10.2f'))              #Uranus weight
print('Weight on Neptune:', format(NEPTUNE, '10.2f'))            #Neptune weight
print('Weight on Pluto:', format(PLUTO, '10.2f'))                #Pluto weight
