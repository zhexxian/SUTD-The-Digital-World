def interlock(word1, word2, word3):
    if word1 == '' or word2 == '' or len(word1) != len(word2):
        return False
    else:
        for i in range(1,len(word1)):
            if word1[0]==word3[0] and word2[0]==word3[1] and word1[i] == word3[2*i] and word2[i] == word3[2*i+1]:
                return True
        return False
            

