def manage_student_database():
    students = []  # List to store student tuples
    student_id = 1  # Start with ID 1
    
    while True:
        student_name = input("Please enter the student's name (or type 'stop' to finish): ")
        
        if student_name.lower() == "stop":
            break
        
        # Check if the name is already in the database
        if any(student[1].lower() == student_name.lower() for student in students):
            print("This name is already in the list.")
        else:
            students.append((student_id, student_name))  # Add student with unique ID
            student_id += 1  # Increment ID for the next student
    
    # Step 4: Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)
    
    # Step 5: Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Step 6: Calculate and display statistics
    total_students = len(students)
    total_name_length = sum(len(student[1]) for student in students)
    longest_name = max(students, key=lambda student: len(student[1]))[1]
    shortest_name = min(students, key=lambda student: len(student[1]))[1]
    
    print("\nTotal number of students:", total_students)
    print("Total length of all student names combined:", total_name_length)
    print("The student with the longest name is:", longest_name)
    print("The student with the shortest name is:", shortest_name)

# Call the function to run the program
manage_student_database()



