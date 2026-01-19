try :
    user_name = input("Enter your name :")
    user_age = float(input("Enter your current Age :"))

    if user_age <= 0:
        print(f"Invalid Age , Age must be greater then zero")
    elif user_age < 13 :
        print(f"Hello {user_name}! As a Child, you have many opportunities ahead")
    elif user_age > 13 and user_age < 17 :
        print(f"Hello {user_name}! As a Teenager, Enjoy your childhood and keep smiling and learning new things!")
    elif user_age > 18 and user_age < 55 :
        print(f"Hello {user_name}! As a Adult ,Keep growing, learning, and moving toward your goals ")
    else :
        print(f"Hello {user_name}! As a Senior ,Your experience and wisdom are truly valuable—keep inspiring others ")

except ValueError :
    print("Error : please enter a valid intergar value")



    






