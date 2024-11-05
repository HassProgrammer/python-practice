from func import *

def main ():
    while True:
        print('\n Student Grades Management System' )
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Search Student")
        print("6. Exit")

        choice = int(input("Enter your choice:\t"))

        if choice == 1:
            name = input("Enter your name:\t")
            grade = int(input("Enter student grade:\t"))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter your name:\t")
            grade = int(input("Enter student grade:\t"))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter your name:\t")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            name = input("Enter your name:\t")
            search_student(name ,grade)
        elif choice == 6:
            print("Closing the program.....")
            break
        else:
            print("Invalid choice. ")
main()