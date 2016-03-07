import time
print "Καλημέρα"
time.sleep(3)
apadisi = 42
print "Η απάντηση είναι...",apadisi

#print "Πως σε λένε ; "
onoma = raw_input("Πως σε λένε ;")


ora = time.localtime().tm_hour

print "Η ώρα τώρα ειναι :", ora
if ora < 14:
    print "Καλημέρα", onoma
else:
    print "Καλησπέρα", onoma    

