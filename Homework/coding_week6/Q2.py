f = open('C:\\Users\\Zhang Zhexian\\Downloads\\week_06\\replace1.txt','r')

def replace(f, oldS, newS):
    lines = f.readline()
    a = ''

    while lines:
        if oldS in lines:
            b = lines.replace(oldS,newS)
            a += (b)
        else:
            a += (lines)
        lines = f.readline()
    return str(a)


    
    
