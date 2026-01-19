try:
    student_marks = float(input("Enter your makrs from 0 to 100 :"))

    if student_marks < 0 or student_marks > 100 :
        print("Please enter marks between 0 to 100")
    elif student_marks >= 90 and student_marks <= 100 :
        print("Grade:A:'Excellent work!'")
    elif student_marks >= 80 and student_marks <= 89 :
        print("Grade:B:'Good Job'")
    elif student_marks >= 70 and student_marks <= 79 :
        print("Grade:C :Nice try , Keep improving ")
    elif  student_marks >= 60 and student_marks <= 69 :
        print("Grade:D:You passed , But ther are many things to improve")
    else :
        print("Grade:F:Failure is only the opportunity more intelligently to begin again.")
except ValueError :
    print("Invalid value : please enter valid integar value")
    