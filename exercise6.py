num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0 :
    print ("Bigyan ng jacket!")

elif num % 3 == 0 :
    print ("Hep! Hep!")

elif num % 5 == 0 :
    print ("Horaaay!")

else :
    print (f"{num} Tawsan!")

#create a program that accepts user input and if divisible by 3, print "Hep! Hep!"