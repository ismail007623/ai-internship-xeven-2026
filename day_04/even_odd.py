try :
    num1 = float(input("Enter a value :"))

    if num1 % 2 == 0:
        print("Number is Even")
    else :
        print("Number is Odd")

except ValueError :
    print("Error: invalid value")