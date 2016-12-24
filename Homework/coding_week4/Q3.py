####### Your function should return a tuple containing a list of average #####
####### and the overall average, e.g., ([3.5,6.0,1.4], 3.625) ################  

def findAverage(listOfLists):
    a = []
    b = c = 0
    for i in listOfLists:
        b += sum(i)
        c += len(i)
        if i == []:
            a.append(0.0)
        else:
            a.append(sum(i)/float(len(i)))
        
    return (a, b/float(c) )



