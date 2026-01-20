try :
    user_age = input("Enter your age :")
    is_tuseday = input("is today Tuseday (yes/no)").strip().lower()
    is_blaclisted = False
    movie_ticket_price = 12
    discount = 0

    if not is_blaclisted :
        if is_tuseday :
            discount = movie_ticket_price * 0.5
            print(f"Congrates you get 50% off :{movie_ticket_price} after discount :",discount)
        elif user_age < 12 or user_age > 65 :
            print("You got 20% dicscount")
    else :
        print("Acsess denied Member is in  blacklist")
        
except ValueError :
    print("Please enter a valid value")