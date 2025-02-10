lname = input('Enter Last Name: ')
fname = input('Enter First Name: ')
age = input('Enter Age: ')
contact = input("Enter Contact Number: ")
course = input("Enter Course: ")

stud_info = f'Last Name: {lname} \nFirst Name: {fname} \nAge: {age} \nContact Number: {contact} \nCourse: {course}'
file = open('students.txt', 'a')
file.write(stud_info)
print("Student Information has been saved to 'students.txt.'")