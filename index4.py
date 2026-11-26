#WAC to store word meaning in dictionary and print the meaning of word entered by user.

# "table": "An item of furniture", "list of facts & figures" 
#"cat": "A small animal."


dict= {

    "table": ["An item of furniture", "list of facts & figures"],
    "cat": "A small animal."
}

print(dict)

#WAC to find no. of classroom we need according to the list of subjects (SETS)

subjects = { "python", "java", "C++", "python", "javaScript", "C++", "python", "java", "C", "java"}


print("Number of classroom we need:", len(subjects))

# WAP to enter marks of 3 subjects from user & store them in a dictionary. Start with empty dictionary and add one by one, use subjects as key and marks as value. Print the dictionary.

total_marks={}

subject1= input("Enter your first subject:")
marks1= int(input("Enter your first subject marks:"))
total_marks.update({subject1:marks1})
subject2= input("Enter your second subject:")
marks2= int(input("Enter your second subject marks:"))
total_marks.update({subject2:marks2})
subject3= input("Enter your third subject:")
marks3= int(input("Enter your third subject marks:"))
total_marks.update({subject3:marks3})   

print("Marks Dictionary:", (total_marks))


#WAP to store 9, 9.0 in a set as a seprate element and print the set.

value1= ("float", 9.0)
value2= ("int", 9)

set={value1, value2}

print(set)
