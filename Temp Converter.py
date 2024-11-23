#Welcome message with name.
print('Jose\'s Temp Converter')

#Ask user for temperature.
nTemp = float(input('Enter a temperature: '))

#Ask user is the temperature entered is fahrenheit or celcius.
sUnit = input('Is the temp F for fahrenheit or C for celsius? ')

#Calculate the equivalent temp conversion for the user's input.
#Temp for C can not be greater than 100.
if nTemp > 100 and sUnit == 'C':
    print('Temp can not be > 100')
elif sUnit == 'C':
    nTemp = float(9.0 / 5.0) * (nTemp) + 32
    print('The Fahrenheit equivalent is: ' f'{nTemp}')

#Temp for F can not be greater than 212.
elif nTemp > 212 and sUnit == 'F':
    print('Temp can not be > 212')
elif sUnit == 'F':
    nTemp = float(5.0 / 9) * (nTemp -32)
    print('The Celsius equivalent is: ' f'{nTemp:.1f}')
else:
    print('You must enter a F or C')
