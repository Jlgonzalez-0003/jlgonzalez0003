#Get the original deposit amount.
nDeposit = int(input('What is the Original Deposit (positive value): '))
if nDeposit < 0:
    print('Input must be a positive numeric value')
    
#Get the interest rate.
nRate = float(input('What is the Interest Rate (positive value): '))
if nRate < 0:
    print('Input must be a positive numeric value')

#Get the number of months.
nMonths = int(input('What is the Number of Months (positive value): '))
if nMonths < 1:
    print('Input must be a positive numeric value')

#Get the goal amount.
nGoal = float(input('What is the Goal Amount (can enter 0 but not negative): '))
if nGoal < 0:
    print('Input must be 0 or greater')

nInterest = nRate / 100 / nMonths
m= 0

while m < nMonths:
    nDeposit = nDeposit * (1 + nInterest)
    m += 1
    print(f'Month: {m}', 'Account Balance is: $',format(nDeposit, ',.2f'))
