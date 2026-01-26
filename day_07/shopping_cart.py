try :
    items = []
    item_price = []
    item_quantity = []

    def display_menu():
        print("Shopping Cart System")
        print("1. Add items in Cart")
        print("2. Remove items in Cart")
        print("3. update items quantity in Cart")
        print("4. Total cart amount")
        print("5. Recently items Add in cart")
        print("6. press 6 for Exit")

    def add_items(name: str , price: int ,quantity: int):
        """
        Add items in shopping cart
        Args:
        name :item name
        price : item price
        quantity : item quantity
        """

        try :
            if name in items :
                 index = items.index(name)
                 item_quantity[index] = item_quantity[index] + quantity
                 print(f"items {items[index]} Add succesfully :{item_quantity[index]}")
            else :
                 items.append(name)
                 item_price.append(price)
                 item_quantity.append(quantity)
                 print(f"Item : {name} Add to cart successfully ")

        except IndexError:
             print("Error :Wrong index")
        except TypeError :
             print("Wrong data type")
 
    def remove_items(name: str ):
        """
        Remove item from cart
        Args :
        name : item name"""

        try :
            if name not in items :
                 print("No items found for this name")
            else :
                 index = items.index(name)
                 items.pop(index)
                 item_price.pop(index)
                 item_quantity.pop(index)

                 print(f"Item : {name} : Removed successfully")
        except IndexError:
             print("Error :Wrong index")
        except TypeError :
             print("Wrong data type")
        
    def update_quantity(name: str , new_quantity: int):
        """
        Update items quantity 
        Args :
        name : item name
        new_quantity : item quantity
        """
        
        try :
            if name in items :
                index = items.index(name)
                if new_quantity <=0 :
                    remove_items(name)
                else :
                    index = items.index(name)
                    item_quantity[index] = new_quantity
                    print(f"items {items[name]} Add succesfully :{item_quantity[index]}")
            else:
                 print(f"No item : {name} found")
            
        except IndexError:
             print("Error :Wrong index")
        except TypeError :
             print("Wrong data type")

    def calculate_total ( ):
        """Calculate total cart price for user"""

        if not items :
            print("Please add items in cart")
        else :

            total = 0
            for i in range(len(items)):
                value = item_price[i] * item_quantity[i]
                total = total + value

            items_length = len(items)
            print(f"Items :{items}")
            print(f"Price :{item_price}")
            print(f"items Quantity :{item_quantity}")
            print(f"Total items lenght {items_length} : ")
            print(f"Total bill  : {total}")

            if total > 100 :
                discount_price = total * 0.10
                grand_total = total - discount_price
                print(f"Bill After 10 per discount : {grand_total}")
    
    def recently_add_items():
        """Recently add items"""

        if not items :
             print("Cart is empty")
    
        else :
             last_three_items = items[-3:]
             print(f"last three items : {last_three_items}")

except IndexError :
    print("Index error")

def main():

    while True :
        display_menu()
        choice = int(input("select between 1 to 5 for shopping , and exit for quit  :"))

        if choice == 1 :
            name = input("Enter Item name : ")
            price = float(input("Enter price :"))
            quantity = float(input("Enter a quantity :"))
            add_items(name , price , quantity)

        elif choice == 2:
            name = input("Enter Item name : ")

            remove_items(name)
        elif choice == 3 :
            name = input("Enter Item name : ")
            quantity = float(input("Enter a quantity :"))
            update_quantity(name , quantity)

        elif choice == 4 :
            calculate_total()

        elif choice == 5:
            recently_add_items()

        elif choice == 6 :
            print("Exit successfuly")
            break

        else :
            print("Please select operation from 1 to 5")

if __name__ == "__main__" :
    main()
           

            







        

            


