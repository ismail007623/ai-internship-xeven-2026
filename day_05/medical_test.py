try :
    age = float(input("enter your age :"))

    if age <= 0:
        print("age must be greater then 0 and non negative")
    elif age > 50 :
        print("Medical test price is 10000")
    else :
        print("Medical test price is 5000")

except ValueError :
    print("Error : Enter valid numeric value")