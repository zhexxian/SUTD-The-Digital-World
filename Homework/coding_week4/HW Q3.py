def nBynMultiplicationTable(N):
    if N < 2:
        return None
    else:
        x = []
        for i in range (1, N+1):
            table=[]

            for j in range (1, N+1):
                table.append (i*j)
            x.append(table)
        return x


# RYAN IS SUPER SMART