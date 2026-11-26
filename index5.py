#WAP to write nos. 1 to 100

i = 1

while i <= 100:
    print(i)
    i += 1


#WAP to write nos. 100 to 1

i = 100

while i >=1:
    print(i)
    i -= 1
    

#WAP to write the table of n

n = int(input ("Enter the no. of which you want to print the table:"))
i = 1
while i <= 10:
    print( n*i )

    i+= 1


#WAP to print the nos. of the following list using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
#traverse on list or tuple to print or action 

#1st method
numbers=[]

i= 1
while i<= 10:
    numbers.append(i*i)
    i+= 1
print(numbers)

#2nd method
list= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
sq=[]
i= 0
while i < len(list):
    sq.append(list[i])
    i+= 1

print(sq)

#WAP to search the no. x from the following tuple:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


