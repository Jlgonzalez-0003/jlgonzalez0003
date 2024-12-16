def getFloatInput(prompt):

    status = False

    while not status:

        try:
            num = float(input(prompt))

            status = True

            if num < 0:

                raise Exception('Value cannot be negative or zero')

        except Exception as e:

            print(e)

            status = False

            return num

#Calculate conversions
def getGallonsOfPaint(wallSqFeet, feetPerGallonPaint):

    return wallSqFeet * feetPerGallonPaint

def getLaborHours(laborHoursPerGallon, totalGallons):

    return totalGallons/laborHoursPerGallon

def getLaborCost(laborHoursPerGallon, paintingChargePerHour):

    return laborHoursPerGallon * paintingChargePerHour;

def getPaintCost(totalGallons, paintPrice):

    return totalGallons * paintPrice

def getSalesTax(state):

    if state == "CT":

        return .06;

    elif state== "MA":

        return .0625

    elif state== "ME":

        return .085

    elif state == "NH":

        return .0

    elif state == "RI":
        
        return .07

    elif state== "VT":

        return .06

    else:

        return 0

def showCostEstimate(laborHours, laborCost, paintCost,tax):

    total = (laborCost*laborHours)+paintCost

    salesTax = total*tax

    total += salesTax

    file = open("PaintJobOutput.txt", "W")

    file.write("Total Paint Cost $(0:.2f)".format(total))

    file.close(print("Total Paint Cost ${0:2f)".format(total)))

# Define main.

def main():

    wallSize = getFloatInput('Enter wall space in square feet: ')

    paintPrice = getFloatInput('Enter paint price per gallon: ')

    feetPerGallonPaint = getFloatInput('Enter feet per gallon: ')

    laborHoursPerGallon = getFloatInput('How many labor hours per gallon: ')

    laborChargePerHour = getFloatInput('Labor Charge per hour: ')

    state = input('State job is in: ')

    paintRequired = getGallonsOfPaint(wallSize, feetPerGallonPaint)

    totalLaborHours = getLaborHours(laborHoursPerGallon, paintRequired)

    totalLaborCost = getLaborCost(laborHoursPerGallon, laborChargePerHour)

    paintCost = getPaintCost(paintRequired, paintPrice)

    tax = getSalesTax(state)

    showCostEstimate (totalLaborHours, totalLaborCost, paintCost, tax)

main()
