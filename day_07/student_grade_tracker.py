try:
    student_names = ['ali','hassan','saad','uzair','ahmad' , 'abdullah']
    student_marks = [66 , 76, 89, 34 , 77 ,93]

    print("***Students Mangement System***")
    print(f"Students :{student_names}")
    print(f"Marks :{student_marks}")
    print(f"Total Number of students {len(student_names)}")


    def add_students(name:str , marks : int) :
        """ 
        To add new student in system
           Agrs:
           name : Student name
           marks :student marks 
        """

        student_names.append(name)
        student_marks.append(marks)

        print(f"Student : {name} : with  Marks :{marks} : Added successfully")
        print(f"List updated successfully : {student_names} , {student_marks}")

    add_students('umar', 76)


    def remove_students(name : str  , marks : int) :
        """ 
        To remove students in system
        Args:
        name : student name
        marks : students marks
        """

        student_names.remove(name)
        student_marks.remove(marks)

        print(f"Student : {name} : with  Marks :{marks} : removed successfully")
        print(f"List updated successfully : {student_names} , {student_marks}")

    remove_students('ali' , 66)


    def update_students_marks( ):
        """Update students marks in system """
        
        student_marks[0] = 99
        print(student_marks)
    update_students_marks()


    def get_avrg():
        """Calculate Avrg makrs of students"""

        avrg_marks = sum(student_marks)/ len(student_marks)
        
        print(avrg_marks)

    get_avrg()


    #find highest Students marks
    highest_marks = max(student_marks)
    index = student_marks.index(highest_marks)
    name = student_names[index]
    print(f"Student : {name}: with highest Marks :{highest_marks}")

    #find minimum marks students in list 
    lowest_marks = min(student_marks)
    index = student_marks.index(lowest_marks)
    name = student_names[index]
    print(f"Student : {name}: with Lowest Marks :{lowest_marks}")

    #sort students by grade
    student_marks.sort(reverse=True)
    print(f"Sort student in Descending order :{student_marks}")
    top_three_performer = student_marks[:3] 
    print(f"Top three Performer of the class : {top_three_performer}")

    #above avrg students
    above_avrg = [i for i in student_marks if i > 78]
    print("Above avrg :",above_avrg)

    #below avrg students
    below_avrg = [i for i in student_marks if i < 78]
    print("Below avrg :",below_avrg)


except IndexError:
    print("Error: Wrong index")
except ValueError :
    print("Wrong Data type")