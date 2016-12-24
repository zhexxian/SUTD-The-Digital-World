f = open('C:\\Users\\Zhang Zhexian\\Downloads\\week_06\\file.txt.txt','r')
def senSplit(f):
    retval=[]
    total = ''
    line = f.readline()
    line.strip()
    while line:
        total += line
        line = f.readline()


    total = splitjoin(total,'.')
    total = splitjoin(total,'?')
    total = splitjoin(total,'!')

    retval=total.split('||')    
    f.close()
    

    ########## Add your code below this line. ##################################
    ########## f is the file object after opening text file ######
    ########## as defined in the handout #######################
    
    
    ######### Ignore code below this line ######################################
    
    return retval


def splitjoin(fstr,sep):
    titles = ['Mr.','Mrs.','Dr.']
    punct = ['.',',','?','!']

    mystrlist=fstr.partition(sep)

    first=mystrlist[0]+mystrlist[1]
    second=mystrlist[2]

    if (second == ''):
        return first
    elif(len(second)<=1):
        return first+second
    elif (first in titles):
        return first+splitjoin(second,sep)
    elif (second[0] != ' ' and second[0].islower()):
        return first+splitjoin(second,sep)
    elif(second[0] != ' ' and second[0].isalnum()):
        return first+splitjoin(second,sep)
    elif(second[0].isspace() and second[1].islower()):
        return first+splitjoin(second,sep)
    elif(second[0] in punct):
        return first+splitjoin(second,sep)
    else:
        return first+'||'+splitjoin(second.lstrip(),sep)


