#Get the user's name and wieght.
sName=input('What is your name? ')
nWeight=float(input('What is your weight? '))
#Get the weight of user by calculating (earth weight x planets Surface Gravity Factor).
#Calculate weight planets.
nMERCURY_SGF = 0.38
nVENUS_SGF = 0.91
nMOON_SGF = 0.165
nMARS_SGF = 0.38
nJUPITER_SGF = 2.34
nSATURN_SGF = 0.93
nURANUS_SGF = 0.92
nNEPTUNE_SGF = 1.12
nPLUTO_SGF = 0.066

#Display planets #Display user's name and the statement ' here are your weights on our Solar System's
#planets:'.
print(sName, 'here is your weights on our Soloar System\'s planets:')
#Display the weights for the corresponding planets.
print(f'{'Weight on Mercury:':25s}{nWeight * nMERCURY_SGF:10.2f}lb')       #Mercury weight
print(f'{'Weight on Venus:':25s}{nWeight * nVENUS_SGF:10.2f}lb')           #Venus weight
print(f'{'Weight on Moon:':25s}{nWeight * nMOON_SGF:10.2f}lb')             #Moon weight
print(f'{'Weight on Mars:':25s}{nWeight * nMARS_SGF:10.2f}lb')             #Mars weight
print(f'{'Weight on Jupiter:':25s}{nWeight * nJUPITER_SGF:10.2f}lb')       #Jupiter weight
print(f'{'Weight on Saturn:':25s}{nWeight * nSATURN_SGF:10.2f}lb')         #Saturn weight
print(f'{'Weight on Uranus:':25s}{nWeight * nURANUS_SGF:10.2f}lb')         #Uranus weight
print(f'{'Weight on Neptune:':25s}{nWeight * nNEPTUNE_SGF:10.2f}lb')       #Neptune weight
print(f'{'Weight on Pluto:':25s}{nWeight * nPLUTO_SGF:10.2f}lb')           #Pluto weight
