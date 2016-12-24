from collections import defaultdict
f = open('C:\\Users\\Zhang Zhexian\\Desktop\\New Text Document.txt','r')

def load_words(f):
    return [word.rstrip() for word in f]

def findAnagram(f):
    t = load_words(f)
    outp = []
    a = []
    b=[]
    b2=[]
    count = 0
    dic= {}
    for i in t:
        check = str(sorted(list(i)))
        
        
        if check not in dic:
            
            dic[check]= 1
        else:
            dic[check] += 1
        
    for j in dic:
        if dic[j] > count:
            count = dic[j]
    
    
    for i in t:
        for j in dic:
            if dic[j] == count:
                                      
                if str(sorted(list(i))) == j:
                    a.append(i)
                    dic[j] = 0

    
        
    for zx in range (len(a)):
        b=[]
        for i in t:
            
            if str(sorted(list(i))) == str(sorted(list(a[zx]))):
                b.append(i)
                if b not in outp:
                    outp.append(b)

      
    
      
                
    


    
                
    return outp
                

        
    
    

