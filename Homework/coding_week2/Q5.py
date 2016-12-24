monthlySaving = input('Enter the monthly saving amount:')
annualInterest = input ('Enter annual interest rate:')

def compoundVal6Months (monthlySaving, annualInterest):
    monthlyInterest = annualInterest / 12.0
    n = 6
    gp = (-1.0 / monthlyInterest) * ((1 + monthlyInterest) * (1 - (1 + monthlyInterest) ** n))
    result = monthlySaving * gp
    return result
    
print 'After the sixth month, the account value is %s' %(compoundVal6Months (monthlySaving, annualInterest))

# use for loop