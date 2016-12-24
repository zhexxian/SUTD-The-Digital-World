def compoundVal6Months(monthlyAmt, annualRate, months):
    monthlyRate = annualRate / 12.0
    result = 0
    for i in range(months):
        result = (monthlyAmt+result) * (1 + monthlyRate)
    return round(result,2)       
    
    
    
