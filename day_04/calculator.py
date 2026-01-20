try :
    num1 = float (input("Enter a 1st value :"))
    num2 = float (input("Enter a 2nd value :"))
    opreator = input("Select Methods From (+,-,*,/,**,%) :")

    if opreator == "+":
        result = num1 + num2
        print(f"{num1}+{num2} =", result)
    elif opreator == "*":
        result = num1 * num2
        print(f"{num1}*{num2} =", result)
    elif opreator == "-":
        result = num1 - num2
        print(f"{num1}-{num2} =", result)
    elif opreator == "/":
        result = num1 / num2
        print(f"{num1}/{num2} =", result)
    elif opreator == "%":
        result = num1 % num2
        print(f"{num1}%{num2} =", result)
    elif opreator == "**":
        result = num1 ** num2
        print(f"{num1}**{num2} =", result)
    else :
        print("Please select between + , _ , / , * , ** , %")

except ValueError:
    print("Please select valid numeric value")