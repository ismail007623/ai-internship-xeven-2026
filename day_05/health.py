try :
    age = float(input("Enter your age :"))
    blood_pressure = float(input("Enter your BP :"))

    if age > 45 and blood_pressure > 140:
        print("Disease")
    else :
        print("No Disease")

except ValueError :
    print("Error : enter a valid numeric value")
    