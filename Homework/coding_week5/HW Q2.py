import math
def leapYear(year):
    if year%4.0 != 0.0:
        return False
    elif year%100.0 != 0.0:
        return True
    elif year%400.0 != 0.0:
        return False
    else:
        return True


def R(y,x):
    return y % float(x)

def dayOfWeekJan1(year):
    if year not in range (1800, 2100):
        return 'Year must be between 1800 and 2099'
    else:
        d = R(1+5*R(year - 1,4) + 4 * R(year - 1, 100) + 6 * R(year - 1, 400), 7)
        return int(d)
        


def numDaysInMonth(month_num,leap_year):
    if month_num not in range(1,13):
        return 'Month number must be in the range of 1 to 12'
    elif month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num in [4,6,9,11]:
        return 30
    elif leap_year == True:
        return 29
    else:
        return 28
        
monthNumCheck = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    if month_num not in range(1,13) or first_day_of_month not in range(0,7):
        return 'Please check your month number and first day again'
    else:
        m = monthNumCheck[month_num]


        wk1 = ''
        wk2 = ''
        wk3 = ''
        wk4 = ''
        wk5 = ''
        wk5a = ''
        wk6 = ''
        for i in range(0,7):
            if i == 0 and i != first_day_of_month:
                wk1 +='  '
            elif i == 0 and i == first_day_of_month:
                wk1 +=' 1'
            elif i<first_day_of_month:
                wk1 +='   '
            else:
                wk1 += '  %d'%(i-first_day_of_month+1)
        for i in range(8-first_day_of_month, 15-first_day_of_month):
            if i == 8-first_day_of_month:
                wk2 +=' %d'%(i)
            elif i<10:
                wk2 +='  %d'%(i)
            else:
                wk2 += ' %d'%(i)
                
        for i in range(15-first_day_of_month, 22-first_day_of_month):
            if i == 15-first_day_of_month and i < 10:
                wk3 +=' %d'%(i)
            elif i == 15-first_day_of_month:
                wk3 +='%d'%(i)
            elif i<10:
                wk3 +='  %d'%(i)
            else:
                wk3 += ' %d'%(i)
        for i in range(22-first_day_of_month, 29-first_day_of_month):
            if i == 22-first_day_of_month:
                wk4 +='%d'%(i)
            else:
                wk4 += ' %d'%(i)
        for i in range(29-first_day_of_month, num_days_in_month+1):
            if i == 29-first_day_of_month:
                wk5a +='%d'%(i)
            else:
                wk5a += ' %d'%(i)
        for i in range(29-first_day_of_month, 36-first_day_of_month):
            if i == 29-first_day_of_month:
                wk5 +='%d'%(i)
            else:
                wk5 += ' %d'%(i)
        for i in range(36-first_day_of_month, num_days_in_month+1):
            if i == 36-first_day_of_month:
                wk6 +='%d'%(i)
            else:
                wk6 += ' %d'%(i)
        
        if wk6 == '' and wk5a == '':
            return [m,wk1,wk2,wk3,wk4]
        elif wk6 == '':
            return [m,wk1,wk2,wk3,wk4,wk5a]
        else:
            return [m,wk1,wk2,wk3,wk4,wk5,wk6]
'''better way to define week:
def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    a=[]
    if month_num==1:
        a.append('January')
    elif month_num==2:
        a.append('February')
    elif month_num==3:
        a.append('March') 
    elif month_num==4:
        a.append('April')
    elif month_num==5:
        a.append('May')
    elif month_num==6:
        a.append('June')
    elif month_num==7:
        a.append('July')
    elif month_num==8:
        a.append('August')
    elif month_num==9:
        a.append('September')
    elif month_num==10:
        a.append('October')
    elif month_num==11:
        a.append('November')
    else:     
        a.append('December')
    j=1
    while j<=num_days_in_month:
        week=''
        for i in range(7):
            if j>num_days_in_month:
                break
            if i!=first_day_of_month and j==1:
                week+='  '
            elif j<10:
                week+=' '
                week+='%s'%j
                j+=1
            else:
                week+='%s'%j
                j+=1
            if i!=6  and j!=num_days_in_month+1:
                week+=' '          
        a.append(week)
    for i in a:
        print i
    return a
'''
        
                
                                
def firstDayOfMonth(year,monthNum):
    if monthNum == 1:
        return dayOfWeekJan1(year)
    daysPast=0
    for i in range(1,monthNum):
        daysPast += numDaysInMonth(i,leapYear(year))
    if daysPast%7 + dayOfWeekJan1(year) > 6:
        return daysPast%7 + dayOfWeekJan1(year) - 7
    return daysPast%7 + dayOfWeekJan1(year)
    
                

def constructCalYear(year):
    if year not in range (1800, 2100):
        return 'Year must be between 1800 and 2099'
    c = [year]
    for i in range(1,13):
        month = constructCalMonth(i, firstDayOfMonth(year,i), numDaysInMonth(i,leapYear(year)))
        
        c.append(month)
    return c


def displayCalendar(year, month):
    if month == None:
        constructCalYear(year).remove(year)
        outp = ''
        for i in range(1,13):
            b=constructCalYear(year)[i][0]
            c=' S  M  T  W  T  F  S'
            d = ''
            for j in range(2,len(constructCalYear(year)[i])+1):
                if i == 12 and j == len(constructCalYear(year)[12]):
                    d+=constructCalYear(year)[i][j-1]

                
                else:
                    d += constructCalYear(year)[i][j-1] + '\n'
            if i < 12:
                outp +=  b + '\n' + c + '\n' + d + '\n'
            else: 
                outp +=  b + '\n' + c + '\n' + d + '\n'
              
        return outp
    else:
        constructCalYear(year).remove(year)
        outp = ''
        b=constructCalYear(year)[month][0]
        c=' S  M  T  W  T  F  S'
        d = ''
        for j in range(2,len(constructCalYear(year)[month])+1):
            d += constructCalYear(year)[month][j-1] + '\n'
        outp +=  b + '\n' + c + '\n' + d
              
        return outp
        



