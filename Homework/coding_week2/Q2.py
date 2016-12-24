def yearsDays(min):
    years = min / (365 * 24 * 60)
    Days = (min % (365 * 24 * 60)) / (24 * 60)
    return (years, Days)
    

#Test Program
a = raw_input('Enter the number of minutes:')
def f(a):
    a = int(a)
    years = a / (365 * 24 * 60)
    Days = (a % (365 * 24 * 60)) / (24 * 60)
    print '%s minutes is approximately %s years and %s days.'%(a, years, Days) 
