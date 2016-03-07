# -*- coding: utf-8 -*-
listalekseon = ["loksa", "net" , "linux" , "methodos"]


def artikol(listalek):
    res = ""
    for i in range(0,len(listalek)):
        res = res + listalek[i][0] 
    return res

print "ή λίστα λέξων είναι",listalekseon 
artikol(listalekseon)
print "και το αρτικόλεκσο είναι το : " , artikol(listalekseon)
    
