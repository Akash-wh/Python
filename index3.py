# Lists & Tuples

# WAP to input 3 fav movies name and create a list of those movies and print the list.
fav_movies = []

movie1 = input("Enter your first favourite movie name: ")

fav_movies.append(movie1)
movie2 = input("Enter your second favourite movie name: ")
fav_movies.append(movie2)
movie3 = input("Enter your third favourite movie name: ")
fav_movies.append(movie3)

print ( fav_movies)

print (type(fav_movies))

#WAP to check the list is palindrome or not.

Marks = []

Marks.append(int(input("Enter your 1st no.: ")))
Marks.append(int(input("Enter your 2nd no.: ")))
Marks.append(int(input("Enter your 3rd no.: ")))
Marks.append(int(input("Enter your 4th no.: ")))    
Marks.append(int (input("Enter your 5th no.: ")))

copy_marks = Marks.copy()

copy_marks.reverse()

print(Marks)
print(copy_marks)

if ( Marks == copy_marks):
    print ("The list is palindrome.")

else:
    print ("The list is not palindrome. ")


# WAP to find the count of A in the tuple and print the count.

Grade = ( "A", "Q", " V", "A", "O", "V", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J")


count = Grade.count ("A")

print ("The count of A in the tuple is:", count)

# WAP to store the above tuple in list & sort the list in ascending order and print the sorted list.

Grade_list = list(Grade)

Grade_list.sort()

print (Grade_list)