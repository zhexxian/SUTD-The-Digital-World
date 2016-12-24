# -*- coding: utf-8 -*-

def moveDisks(n, fromTower, toTower, auxTower,sol):
    
    if n==1:

        sol.append('Move disk 1 from %s to %s'%(fromTower,toTower))

        return sol

    else:

        moveDisks(n-1, fromTower, auxTower, toTower, sol)

        sol.append('Move disk %d from %s to %s'%(n,fromTower,toTower))

        moveDisks(n-1,auxTower,toTower,fromTower,sol)
        
        return sol
        





