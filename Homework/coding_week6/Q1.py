fileName = 'C:\\Users\\Zhang Zhexian\\Downloads\\week_06\\xy.dat'

def read2columns(f):
    infile = f
    lines = infile.readlines()
    y = []

    for i in range(len(lines)):
        x = lines[i].strip().split()
        y.append(float(x[1]))


    a = float(max(y))
    b = float(min(y))
    infile.close()
    return (a,b)
        


