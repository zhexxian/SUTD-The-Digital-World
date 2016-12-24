f = open('C:\\Users\\Zhang Zhexian\\Downloads\\week_06\\constants.txt','r')
def fundamentalConstants(f):
    a = {}
    
    line = f.readline()
    line = f.readline()
    line = f.readline()

    
    while line:
        newline = line.split(' ')
        for i in range(1,len(newline)-1):
            if newline[i] != '':
                a[newline[0]] = float(newline [i])
                

        line = f.readline()
    return a
        

    f.close()

