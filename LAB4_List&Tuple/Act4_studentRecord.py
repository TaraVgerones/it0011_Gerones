students = []  
filename = ''

# Menu
while True:
    print("=" * 40)
    print(" STUDENT RECORD MANAGEMENT ".center(40, '='))
    print("[1]. Open File")
    print("[2]. Save File")
    print("[3]. Save As File")
    print("[4]. Show All Students Record")
    print("[5]. Show Student Record")
    print("[6]. Add Record")
    print("[7]. Edit Record")
    print("[8]. Delete Record")
    print("[0]. Exit")
    print("=" * 40)
    choice = input("Enter your choice: ")

    # Open File
    if choice == '1':
        filename = input('Enter the file name you want to open: ')
        try:
            file = open(filename, 'r')
            lines = file.readlines()
            #students = []
            for i in range(0, len(lines), 4):
                student_id = lines[i].strip().split(": ")[1]
                full_name = lines[i+1].strip().split(": ")[1].split(" ")
                class_standing = float(lines[i+2].strip().split(": ")[1])
                major_exam = float(lines[i+3].strip().split(": ")[1])
                students.append([student_id, (full_name[0], full_name[-1]), class_standing, major_exam])
            file.close()
            print("-" * 40)
            print("File opened successfully.")
            print("-" * 40)
        except FileNotFoundError:
            print("-" * 40)
            print("File not found.")
            print("-" * 40)

    # Save File
    elif choice == '2':
        if filename:
            file= open(filename, 'w')
            for student in students:
                file.write(f"Student ID: {student[0]}\n")
                file.write(f"Student Name: {student[1][0]} {student[1][1]}\n")
                file.write(f"Student Class Standing: {student[2]}\n")
                file.write(f"Major Exam Grade: {student[3]}\n")
            file.close()
            print("-" * 40)
            print(f'Record saved to {filename}')
            print("-" * 40)
        else:
            print("-" * 40)
            print("No file opened. Use 'Save As' to specify.")
            print("-" * 40)

    # Save As File
    elif choice == '3':
        filename = input('Enter file name: ')
        file = open(filename, 'w')
        for student in students:
            file.write(f"Student ID: {student[0]}\n")
            file.write(f"Student Name: {student[1][0]} {student[1][1]}\n")
            file.write(f"Student Class Standing: {student[2]}\n")
            file.write(f"Major Exam Grade: {student[3]}\n")
        file.close()
        print("-" * 40)
        print(f"File Saved as {filename}.")
        print("-" * 40)

    # Show All Students Record
    elif choice == '4':
        if not students:
            print("-" * 40)
            print("No student records available.")
            print("-" * 40)
            continue
        
        print("=" * 40)
        print("Show All Students Record Options:")
        print("=" * 40)
        print("[1]. Order by Last Name")
        print("[2]. Order by Grade")
        print("-" * 40)
        showRecord_choice = input('Enter your choice: ')

        #Show by last name
        if showRecord_choice == '1':
            print("\nShow Student Record by Last Name")
            print("=" * 80)
            print(f"{'ID':^6} {'Last Name':^13} {'First Name':^16} {'Class Standing':^16} {'Exam Grade':^16}")
            print("=" * 80)
            for i in range(len(students)):
                for j in range(i + 1, len(students)):
                    if students[i][1][1] > students[j][1][1]:
                        students[i], students[j] = students[j], students[i]
            for student in students:
                print(f"{student[0]:<8} {student[1][1]:<15} {student[1][0]:<15} {student[2]:<15} {student[3]:<10}")
                print("=" * 80)
                
        #show by grade
        elif showRecord_choice == '2':
            print("\nShow Student Record by Grade")
            print("=" * 80)
            print(f"{'ID':^6} {'Last Name':^13} {'First Name':^15} {'Class Standing':^16} {'Exam Grade':^16}")
            print("=" * 80)
            for i in range(len(students)):
                for j in range(i + 1, len(students)):
                    grade_i = students[i][2] * 0.6 + students[i][3] * 0.4
                    grade_j = students[j][2] * 0.6 + students[j][3] * 0.4
                    if grade_i > grade_j:
                        students[i], students[j] = students[j], students[i]
            for student in students:
                print(f"{student[0]:<9} {student[1][1]:<15} {student[1][0]:<15} {student[2]:<15} {student[3]:<10}")
                print("=" * 80)
        else:
            print("-" * 40)
            print("Invalid Choice.")
            print("-" * 40)
            continue

    # Show Student Record
    elif choice == '5':
        showRecord = ' SHOW STUDENT RECORD '
        print(showRecord.center(40, '='))
        
        search_id = input("Enter Student ID: ")
        print("-" * 40)
        for student in students:
            if student[0] == search_id:
                print(f"Student ID: {student[0]} \nName: {student[1][0]} {student[1][1]} \nClass Standing: {student[2]} \nMajor Exam: {student[3]}")
                break
        else:
            print("-" * 40)
            print("Student not found.")
            print("-" * 40)

    # Add Record
    elif choice == '6':
        addRecordf = ' ADD RECORD '
        print(addRecordf.center(40, '='))
        
        while True:
            stu_id = input("Enter Student ID (6 digits): ")
            if len(stu_id) == 6 and stu_id.isdigit():
                break
            print("-" * 40)
            print("Invalid! Student ID must be exactly 6 digits.")
            print("-" * 40)
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Exam Grade: "))
        students.append([stu_id, (f_name, l_name), class_standing, major_exam])
        print("-" * 40)
        print("Student Record Added Successfully.")
        print("-" * 40)

    # Edit Record
    elif choice == '7':
        editRecord = ' EDIT RECORD '
        print(editRecord.center(40, '='))
        
        stu_id = input("Enter Student ID to edit: ")
        
        for i in range(len(students)):
            if students[i][0] == stu_id:
                while True:
                    print("=" * 40)
                    print("What do you want to edit?")
                    print("=" * 40)
                    print("[1] Student ID")
                    print("[2] Name")
                    print("[3] Class Standing")
                    print("[4] Major Exam Grade")
                    print("[0] Go Back")
                    print("-" * 40)
                    edit_choice = input("Enter your choice: ")

                    if edit_choice == '1':
                        new_id = input("Enter new Student ID: ")
                        students[i][0] = new_id if new_id else students[i][0]
                        print("-" * 40)
                        print("Student ID updated successfully!")
                        print("-" * 40)

                    elif edit_choice == '2':
                        new_f_name = input("Enter new First Name: ") or students[i][1][0]
                        new_l_name = input("Enter new Last Name: ") or students[i][1][1]
                        students[i][1] = (new_f_name, new_l_name)
                        print("-" * 40)
                        print("Student Name updated successfully!")
                        print("-" * 40)

                    elif edit_choice == '3':
                        new_class_standing = input("Enter new Class Standing: ")
                        students[i][2] = float(new_class_standing) if new_class_standing else students[i][2]
                        print("-" * 40)
                        print("Class Standing updated successfully!")
                        print("-" * 40)

                    elif edit_choice == '4':
                        new_major_exam = input("Enter new Major Exam Grade: ")
                        students[i][3] = float(new_major_exam) if new_major_exam else students[i][3]
                        print("-" * 40)
                        print("Major Exam Grade updated successfully!")
                        print("-" * 40)

                    elif edit_choice == '0':
                        break

                    else:
                        print("-" * 40)
                        print("Invalid choice. Please try again.")
                        print("-" * 40)
                
                print("-" * 40)
                break  
        
        else:
            print("-" * 40)
            print("Student not found.")
            print("-" * 40)

    # Delete Record
    elif choice == '8':
        deleteRecord = ' DELETE RECORD '
        print(deleteRecord.center(40, '='))
        
        stu_id = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i][0] == stu_id:
                del students[i]
                print("-" * 40)
                print("Record deleted.")
                print("-" * 40)
                break
        else:
            print("-" * 40)
            print("Student not found.")
            print("-" * 40)

    # Exit
    elif choice == '0':
        print("-" * 40)
        print("Thank you. Have a Nice Day!")
        print("-" * 40)
        break
    else:
        print("-" * 40)
        print("Invalid choice. Try again.")
        print("-" * 40)
