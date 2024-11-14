#Get the starting principal.
nPrincipal = int(input('Enter the starting principal: '))

#Get the interest rate.
nRate = float(input('Enter the annual interest rate: '))

#Get the how many times per year the interest is compounded.
nCompound = int(input('How many times per year is the interest compounded? '))

#Get how many years the investment will earn interest.  
nYears = int(input('For how many years will the account earn interest? '))

#Calculate the future value by calculating the time and interest rate in which the
#investment will be compounding.
nFuture_value = nPrincipal *(1 + nRate/100/nCompound)**(nCompound * nYears)

#Display the future value after calculations have been made.
print(f'{'At the end of 2 years you will have $'}{nFuture_value: ,.2f}')
