import json

students = {101 :
           {"name":"ismail" , "age":20 , "grade":{"math":50 ,"phy":60}} }

def add_student(student_id: int , name: str , age: int , grade) :
    """Add a new student to the students dictionary.

    Args:
        student_id: Unique student identifier.
        name: Student name.
        age: Student age.
        grade: Dictionary of subject-score pairs.
    """

    if student_id in students :
        return {f"{student_id} : Already exists"}
        
    else :

        students[student_id] = {
                 "name":name ,
                 "age":age,
                 "grade":grade
            }

    return f"student Added successfully : {name}"
    

def update_grade(new_score: int , student_id: int , subject_name: str):
    """Update a student's subject grade.

    Args:
        student_id: Unique student identifier.
        subject_name: Subject name.
        new_score: Updated score.

    Returns:
        Status message indicating result.
    """
  
    if student_id not in students :
         return {f"Student not exists"}
    subjects = students[student_id]["grade"]

    if subject_name not in subjects :
         return  "No subject found for this name"
        
    subjects[subject_name]=new_score
    return  f"subject {subject_name} marks {new_score} updated successfully"
    

def student_avrg(student_id: int):
    """
    Calucluate student Average marks
    Args :
    student id : unique studend id
    """

    if student_id not in students:
         return f"No student exist for this ID :{student_id}"
    
    subjects = students[student_id]["grade"]
    total_score = sum(subjects.values())
    num_subject = len(subjects)

    if num_subject == 0:
         return 0

    return total_score/num_subject


def top_students(students):
    """
    Find top student in dictionary highest marks
    Args :
    students : dictionary overall student
    """

    high_avrg = 0
    top_student_score = None

    for student_id  in students :
        avrg = student_avrg(student_id)
        if avrg > high_avrg :
            high_avrg = avrg
            top_student_score = student_id

    return (high_avrg , top_student_score)


def save_to_file():
    """
    Save student record in json file
    """
    with open ('student.json' ,'w') as file :
         json.dump(students , file , indent=4)


def load_file():
    """Load all student from json file"""

    try:
        with open("student.json",'r') as file :
            return json.load(file)
        
    except FileNotFoundError :
         return {}
    

def generate_report(students):
    """Generate a sorted student performance report.

    Args:
        students: Dictionary containing student records.

    Returns:
        A list of tuples sorted by average score.
    """

    report = []

    for student_id , data in students.items():
        avrg = student_avrg(students , student_id)
        report.append((student_id , data["name"]) , avrg)

    report.sort(key = lambda x:x[2] , reverse=True)

    return report


if __name__ == "__main__" :


    students = load_file()


    while True :

        print("***Student Information system***")
        print("Press 1 for Add student")
        print("press 2 for Update grades")
        print("press 3 for to get Average of Student Marks")
        print("press 4 for Top student")
        print("press 5 for Report of student")
        print("press 6 for exit")
        try:
             choice = int(input("Enter a value between 1 to 5: "))
        except ValueError:
             print("Invalid input")
             break

        match choice:

            case _ if choice == 1: 
             
                 id = int(input("Enter student id:"))
                 name = input("enter your name:")
                 age = int(input("enter your age:"))
                 grade = {}
                 subject = int(input("How many subejct do you have"))

                 for i in range(subject):
                     subject_name = input("Enter subject name :")
                     score = int(input("enter subject score :"))
                     grade[subject_name] = score
                 result = add_student(id , name , age , grade)
                 print(result)

            case _ if choice == 2:
                 new_score = int(input("Enter new score :"))
                 student_id = int(input("Enter your student id :"))
                 subject_name = input("Enter a subject name for you want to update grade")

                 response = update_grade(new_score , student_id , subject_name)
                 print(response)
            
            case _ if choice == 3 :
                 student_id = int(input("Enter your student id :"))
                 avrg = student_avrg(student_id)
                 print(avrg)

            case _ if choice == 4 :
                 top_performer_student = top_students (students)
                 print(top_performer_student)

            case _ if choice == 5:
                 response = generate_report(students)
                 print("Progress report :",response)

            case _ if choice == 6 :
                 print("Sucessfully exits")
                 break

save_to_file()
 


