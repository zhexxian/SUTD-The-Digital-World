amount = input ('Enter investment amount:')
interestRate = input ('Enter annual interest rate:')
years = input ('Enter number of years:')

def investmentVal (amount, interestRate, years):
    months = years * 12.0
    monthlyRate = (interestRate / 12.0) / 100.0
    futureInvestmentValue = amount * (1 + monthlyRate) ** (months)
    futureInvestmentValue = round (futureInvestmentValue, 2)
    return futureInvestmentValue
    
print 'Accumulated value is %s' %(investmentVal (amount, interestRate, years))