# Charles Tranter
# SDEV220
# 11/5/2023
# M02Lab.py
#
# This application will test if a student's GPA is good enough to make the Dean's List or Honor Roll. The user can quit by inputing "ZZZ" as the students
# last name.

while True:
    lastName = input("Student Last Name (Enter ZZZ to quit): ")
    
    if lastName == "ZZZ":
        print("Quitting. Thanks!")
        break

    firstName = input("Student First Name: ")
    studentGPA = float(input("Student GPA: "))

    if studentGPA >= 3.5:
        print(lastName + ", " + firstName + " has made the Dean's List!\n")
    elif studentGPA >= 3.25 and studentGPA < 3.5:
        print(lastName + ", " + firstName + " has made Honor Roll!\n")
