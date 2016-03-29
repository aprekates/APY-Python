# -*- coding: utf-8 -*-
# Δραστηριοτητα 5.8.1 απο το βιβλιο Α.Π.Υ ΕΠΑΛ ΙΤΥ 2015-16

# Βασικες επεξεργασιες λιστων

sum = 0
max = 0
max_count = 0
lista = [] 
while sum <= 1000:
    num = input("Δωσε αριθμό:")
    lista.append(num)
    sum = sum + num
    if num == max:
        max_count = max_count + 1
    if num > max:
        max = num
        max_count = 1


a = lista[len(lista)-1]
def evresi_thesis(lista,a):
    c = 1
    for i in lista:
        if i < a:
            c = c + 1
    return c-1

# αθροισμα
print "Το αθροισμα των αριθμων της λιστας ειναι :" ,sum

# μ.ο
print "Ο μεσος ορος των αριθμων της λιστας ειναι :" , sum / len(lista)

# max
print "Ο μεγιστος αριθμος της λιστας ειναι ο :" , max , "και εμφανιζεται στη λιστα:",max_count," φορες"


print "ο τελευταιος αριθμος που δωθηκε ειναι ο:", lista[len(lista)-1] , "και αν η λιστα ηταν ταξινομημενη θα ειχε την θεση:" , evresi_thesis(lista,a)



        

    
