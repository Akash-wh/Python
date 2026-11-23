# WAP tio input a name & find its length
str1 = input("Enter a name: ")
length_str = len(str1)

print( length_str)

str2 =" $ USD  $ EUR $ INR  $ GBP  $ JPY  $ CNY  $ AUD  $ CAD  $ CHF  $ SEK  $ NZD  $ MXN  $ SGD  $ HKD  $ NOK  $ KRW  $ TRY  $ RUB  $ BRL  $ ZAR"

count = str2.count("$")
print ("The count of $ in the string is:", count)
# # IF condition to check if the name is empty or not

Marks = float(input("Enter your marks: "))

if (Marks >= 90):
    print ("Grade A")
elif ( 90 > Marks and Marks >= 80):
    print ("Grade B")
elif ( 80 > Marks and Marks >= 70):
    print ("Grade C")
elif ( 70 > Marks and Marks >= 60):
    print ("Grade D")
else:
    print ("Pointed Pass")


#nesting 

marks = float(input("Enter your marks: "))  

if ( marks >= 90):

    if (marks >= 95):
        print ("Grade A+")
    else :
        print ("Grade A")
elif ( marks >= 80 and marks < 90):
    if (marks >= 85):
        print ("Grade B+")
    else :
        print ("Grade B")
else:
    print ("Grade C")

# WAP to input a number and check if it is even or odd.


Number = int(input ("Enter a number: "))

if ( Number % 2 == 0):
    print ("ENtered number is the even number.")
else:
    print ("Entered number is the odd number.") 

# WAP to input 3 three numbers and find the largest number among them.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if ( a> b and a> c):
    print ("First number", a, "is the largest number.")
elif (b> a and b> c):
    print ("Second number", b, "is the largest number.")
else:
    print ("Third number", c, "is the largest number.")
    

# WAP to input a number if the number is the multiple of 7 

a = int (input ("Enter the number :"))
if ( a % 7 == 0):
    print ("The number is the multiple of 7.")
else:
    print ("The number is not the multiple of 7.")

