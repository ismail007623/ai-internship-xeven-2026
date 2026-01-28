import json


inventory = {}

def add_product(inventory ,product_id: int , name: str , price: int , quantity: int , category: str):
    """
    Docstring for add_product
    Args:

    """
    if product_id in inventory :
        return f"This prouct Id already exists"

    inventory[product_id] = {
        "name":name,
        "price":price,
        "quantity":quantity,
        "category":category
    }


def update_stock(inventory , product_id , new_quantity: int):
    """
    Docstring for update_stock
    Args:
    """
    if product_id not in inventory:
        return f"This product do not exists"
    
    inventory[product_id]["quantity"] = new_quantity

    return f"Stock updated successfully new stock : {new_quantity}"

def search_by_category(category : str , inventory):
    """
    Docstring for search_by_category
    Args:

    """
    product = []
    for product_id in inventory:
        if inventory[product_id]["category"] == category :
           product.append(inventory[product_id]["name"])
     
    if product :
        return product
    else :
        return f"No product found for this Catgory : {category}"
    

def low_stock_alert(inventory):
    """
    Docstring for low_stock_alert
    
    """

    stock = []

    for i in inventory :
        if inventory[i]["quantity"] <= 5 :
            stock.append(f"{inventory[i]['name']}: {inventory[i]['quantity']} left")


    if stock:
        return stock
    else :
        return "All stock is isufficeint"
    

def total_inventory_value(inventory):
    """
    Docstring for total_inventory_value
        
    """
    if not inventory:
        return "Inventory is empty"
    
    total = 0
    for i in inventory:
        value = inventory[i]["price"] * inventory[i]["quantity"]
        total = total + value

    return total


def average_product_price(inventory):
    """
    Docstring for average_product_price
    
    """

    if not inventory:
        return "Inventory is empty"
    
    total_category = {}
    total_count = {}

    for i in inventory:
        category = inventory[i]["category"]
        price  = inventory[i]["price"]

        if category in total_category :
            total_category[category] += price
            total_count[category] += 1
        else :
            total_category[category] = price
            total_count[category] = 1
    
    category_averages = {}

    for category in total_category :
        category_averages[category] = total_category[category] / total_count[category]

    return category_averages


def inventory_report():
    """
    Docstring for inventory_report
    """
    with open("inventory.json" , 'w') as file :
        json.dump(inventory , file , indent=4)


if __name__ == "__main__":


    while True :

        print("***Inventory Maneger***")
        print("Press 1 for Add prodcut :")
        print("press 2 for Update stock :")
        print("press 3 for to Search by category :")
        print("press 4 for Total inventory value :")
        print("press 5 for average prodcut price :")
        print("press 6 for inventory report :")
        print("press 7 for Low stock alert")
        print("press 8 for Exit :")
        try:
             choice = int(input("Enter a value between 1 to 5: "))
        except ValueError:
             print("Invalid input")
             break

        match choice:

            case _ if choice == 1: 
             
                 id = int(input("Enter product id:"))
                 name = input("Enter product name:")
                 price = int(input("Enter a price:"))
                 quantity = int(input("Enter a quantity"))
                 category = input("Enter prodcut category")

                 result = add_product(inventory, id , name , price , quantity , category)
                 print(result)
          
            case _ if choice == 2:
                 new_stock = int(input("Enter new stcok quantity :"))

                 response = update_stock (new_stock)
                 print(response)

            case _ if choice == 3 :
                category = (input("Enter the categpory you want to search :"))
                response = search_by_category(category , inventory)
                print(response)

            case _ if choice == 4 :
                resposne = total_inventory_value(inventory)
                print(resposne)
                
            case _ if choice == 5:
                resposne = average_product_price(inventory)
                print(resposne)   

            case _ if choice == 6 :
                inventory_report()
                
            case _ if choice == 7 :
                response=low_stock_alert(inventory)
                print(response)


            case _ if choice == 8 :
                print("Successfully exit")
                break
             

    






