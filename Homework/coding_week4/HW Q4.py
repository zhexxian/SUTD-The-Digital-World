from collections import Counter

def mostFrequent(numList):
    dict = Counter(numList)

    vals = dict.values()

    m = max(vals)

    
    result = []
  
    for i in dict:

        if dict[i] == m:
            result.append(i)
    return result

