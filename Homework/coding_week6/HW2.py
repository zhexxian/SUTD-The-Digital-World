f = open('C:\\Users\\Zhang Zhexian\\Downloads\\week_06\\scores.txt','r')

def scores(f):
    total = 0
    count = 0
    line = f.readline()
    
    while line:
        total += float(line)
        count += 1
        line = f.readline()
    return (total,total/count)
    
