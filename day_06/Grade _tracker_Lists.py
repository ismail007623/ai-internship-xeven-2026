try:

    students_name = ['ismail','honey','ahsan','awais','ali']
    students_grade = [76,90,80,65,45]

    highest_grade = max(students_grade)
    high_index = students_grade.index(highest_grade)
    highest_grade_name = students_name[high_index]

    lowest_grade = min(students_grade)
    low_index = students_grade.index(lowest_grade)
    lowest_grade_student_name = students_name[low_index]

    avrg_grade = sum(students_grade) / len(students_grade)

    print(f"Highest grade : {highest_grade} : Student Name : {highest_grade_name} ")
    print(f"Lowest grade : {lowest_grade} : Student Name : {lowest_grade_student_name}")
    print(f"Avrage Marks : ",avrg_grade)

    print("Students Passed:")
    if students_grade[0] >= 50:
        print(f"Name : {students_name[0]} : Grade :{students_grade[0]}")
    if students_grade[1] >=50:
        print(f"Name : {students_name[1]} : Grade :{students_grade[1]}")
    if students_grade[2] >= 50:
        print(f"Name : {students_name[2]} : Grade :{students_grade[2]}")
    if students_grade[3] >= 50:
        print(f"Name : {students_name[3]} : Grade :{students_grade[3]}")
    if students_grade[4] >= 50:
        print(f"Name : {students_name[4]} : Grade :{students_grade[4]}")

except IndexError:
    print("wrong index")
except TypeError:
    print("worng data type")