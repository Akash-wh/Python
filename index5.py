#While Loop
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

search_list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 
i = 0
x = int(input("Search your no.:"))

while i < len(search_list):
    if (search_list[i] == x):
        print ("Value found at index:", i)
        break
    else:
        print("finding....")
    i += 1


# For Loop

#WAP to print the following list elements using for loop
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

sq_list=[1,2,3,4,5,6,7,8,9,10]

p_list = []

for i in sq_list:
    if (i <= 10):
        i = i*i
        p_list.append(i)
    i+= 1
print("List Printed:", p_list)

#WAP to search the number x in the following tuple using for loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x= int(input("Search the number:"))

idx = 0

for i in tup:

    if(i == x):
        print("no. find at index :", idx)
    idx+=1



#RANGE Function

#WAP to print 1 to 100 using for & range


list=[]

for i in range ( 1, 101):
    list.append(i)

print(list)

        
