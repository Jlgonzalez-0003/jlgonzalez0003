#This program is to calculate the averages of the users test scores.
sName = input('Name of person that we are calculating the grades for: ')

#Get the users test scores.
nTest1  = float(input('Test 1: '))
nTest2 = float(input('Test 2: '))
nTest3 = float(input('Test 3: '))
nTest4 = float(input('Test 4: '))

#Ask user if they would like to drop the lowest score.
sDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ")

if nTest1 < 0 or nTest2 <0 or nTest3 < 0 or nTest4 < 0:
    print('Test scores must be greater than 0')
    exit()

#Calculate the user's score average.
nTestScores = (nTest1 + nTest2 + nTest3 + nTest4)

if sDropLowest == 'Y' or sDropLowest == 'y':

    if (nTest1 < nTest2 and nTest1 < nTest3 and nTest1 < nTest4):
        nTestAverage = (nTest2 + nTest3 + nTest4) / 3.0
    elif (nTest2 < nTest3 and nTest2 < nTest4):
        nTestAverage = (nTest1 + nTest3 + nTest4) / 3.0
    elif (nTest3 < nTest4):
        nTestAverage = (nTest1 + nTest2 + nTest4) /3.0
    else:
        nTestAverage = (nTest1 + nTest2 + nTest3) / 3.0

elif(sDropLowest == 'N' or sDropLowest == 'n'):
    nTestAverage = (nTest1 + nTest2 + nTest3 + nTest4) / 4.0
    
else:
    print('You must enter a Y or N')
    exit()

print(sName, 'test average is ',format(nTestAverage,'.1f'))

#Based on the average score print the corresponding letter grade.
if nTestAverage >= 97.0:
    print('Letter grade for the test is: A+')
elif nTestAverage >= 94.0:
    print('Letter grade for the test is: A')
elif nTestAverage >= 90.0:
    print('Letter grade for the test is: A-')
elif nTestAverage >= 87.0:
    print('Letter grade for the test is: B+')
elif nTestAverage >= 84.0:
    print('Letter grade for the test is: B')
elif nTestAverage >= 80.0:
    print('Letter grade for the test is: B-')
elif nTestAverage >= 77.0:
    print('Letter grade for the test is: C+')
elif nTestAverage >= 74.0:
    print('Letter grade for the test is: C')
elif nTestAverage >= 70.0:
    print('Letter grade for the test is: C-')
elif nTestAverage >= 67.0:
    print('Letter grade for the test is: D+')
elif nTestAverage >= 64.0:
    print('Letter grade for the test is: D')
elif nTestAverage >= 60.0:
    print('Letter grade for the test is: D-')
elif nTestAverage <= 59.9:
    print('Letter grade for the test is: F')
