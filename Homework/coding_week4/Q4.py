def TransposeMatrix(a):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    ######Enter your code below ########
    for i in range (3):
        for j in range (3):
            result[j][i] = a[i][j]


    ######Ignore code below ############
    return result