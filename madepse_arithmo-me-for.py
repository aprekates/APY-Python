import random
mystikos = random.randint(1,10)
print "Καλώςήρθες!"
print "θα σκεφτώ έναν τυχαίο αριθμό ανάμεσα στο 1 και στο 10"
print "Εχεις 5 προσπάθειες να τον βρείς"

#madepsia = int(m)
for metritis_prospatheion in range(5):
      print "H ", metritis_prospatheion+1 , "σου προσπάθεια"
      madepsia = input("Μάντεψε τον αριθμό που σκέφτηκα: ")
      if madepsia == mystikos:
            print("Το βρήκες!")
            break
      else:
            if metritis_prospatheion == 4:
                  print "Τελείωσαν οι προσπάθειες σου"
                  break
            print("Προσπάθησε πάλι !")

print "Ο μυστικός μου αριθμός ήταν ο :", mystikos
print("Τέλος παιχνιδιού!")

