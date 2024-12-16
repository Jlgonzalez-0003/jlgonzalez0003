#Define the getFloatInput.
def getFloatInput(string):
    while(True):
        try:
            inputvalue = float(input(string))
            if inputvalue < 0:
                raise Exception('Input a number that is greater than 0.')
            else:
                break
        except ValueError as be:
            print('Only numeric values are allowed')
            continue
        except Exception as e:
            print(e)
            continue
    return float(inputvalue)

#Define the median.
def getMedian(PropertyValueList):
    if(len(PropertyValueList) % 2 == 0):
       index = len(PropertyValueList) // 2
       avg = (PropertyValueList[index] + PropertyValueList[index - 1]) / 2
       return avg
    else:
        index = len(PropertyValueList) // 2
        return PropertyValueList[index] 

#Define the main.
def main():
    PropertyValueList = []
    while(True):
        PropertyValueList = getFloatInput('Enter property sales value: ')
        option = input('Enter another value Y or N: ')
        while(not(option == 'y' or option == 'Y' or option == 'n' or option == 'N')):
            option = input('Enter another value Y or N: ')
        if(option == 'y' or option == 'Y'):
            continue
        elif(option == 'n' or option == 'N'):
            break;

#Sort the list.
    PropertyValueList.sort()
    totalsum = 0
    
#Display the property value.
    for i in range(len(PropertyValueList)):
        print('Property ',i,'${:,.2f}'.format(PropertyValueList[i]))
        totalsum = totalsum + PropertyValueList[i]
        
#Display the minimum, maximum, total, average, and comission.
        print('Minimum    :    ${:,.2f}'.format(PropertyValueList[0]))
        print('Maximum    :    ${:,.2f}'.format(PropertyValueList[len(PropertyValueList) - 1]))
        print('Total      :    ${:,.2f}'.format(totalsum))
        print('Average    :    ${:,.2f}'.format(totalsum / len(PropertyValueList)))
        print('Median     :    ${:,.2f}'.format(getMedian(PropertyValueList)))
        print('Commission :    ${:,.2f}'.format(totalsum * 0.03))
        
main()
