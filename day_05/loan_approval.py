try:
    age = float(input("Enter your age :"))
    income = float(input("Enter your income:"))
    credit_score = float(input("Enter your credit score:"))

    if age < 18 :
        print("Decision path: check age < 18")
        print("Age must be over 18")
    elif income < 30000:
        print("Decision path: Age ok now check income < 30000")
        print("Loan reject sallery must be greater then 30000")
    elif credit_score < 600 :
        print("Decision path: Age ok income ok now check credit score")
        print("Loan reject score must be gteather then 600")
    else :
        print("Decision path:Age ok income ok credit score ok")
        print("Congrats Loan Approved")

except ValueError:
    print("Error:enter valid numeric value")