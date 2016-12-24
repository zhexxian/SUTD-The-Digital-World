fileName = 'C:\\Users\\Zhang Zhexian\\Downloads\\data1.txt'

infile = open(fileName, 'r')
lines = infile.readlines()
mysum = 0
for x in lines:
    y = float(x)
    mysum +=y
print float(mysum)/len(lines)
infile.close()