# -*- coding: utf-8 -*-
leksi = raw_input("Δώσε λέξη προς έλεγχο: ")

symmetriki = True
i=0
j=len(leksi)-1

while i < j and symmetriki == True:
    print "i=",i,"-- j=",j 
    if leksi[i] != leksi[j] :
        symmetriki = False
    i = i +1
    j = j -1

if symmetriki == True:
    print "η λέξη: " , leksi , " είναι συμμετρική"
else:
    print "η λέξη: " , leksi , " ΔΕΝ είναι συμμετρική"

