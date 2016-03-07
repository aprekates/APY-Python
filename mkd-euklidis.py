# -*- coding: utf-8 -*-
def mkd(a,b):
    while b > 0:
        # εναλλακτικό ποιό συμπηκνωμένο συντακτικό με χρήση πλειάδας
        #a,b  = b , a%b   
        tmp = a%b
        a = b
        b = tmp
        print 
        print a,",",b
    return a

a = input("Δώσε α:")
b = input("Δώσε β:")
print "Για τους αριθμούς α:",a,",β:",b," o ΜΚΔ είναι:" ,mkd(100,36)
