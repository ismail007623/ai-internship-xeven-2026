try :
    user_age = float(input("Enter your age :"))
    has_document = (input("You have document ? :(Yes/Not)")).lower()

    if user_age >= 18  and has_document == "yes":
        print("Access granted for driving ")
    elif user_age < 18:
       print("Access Denied age must be over 18")
    else :
        print("Dcoument missing Access dinied")
except ValueError:
    print("Enter valid inetagr value")
