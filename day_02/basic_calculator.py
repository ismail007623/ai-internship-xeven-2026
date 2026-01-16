try :
    """
    This program prompts the user to enter two numeric values and performs
    basic arithmetic operations (sum, difference, product, and quotient).
    It includes error handling for invalid input and division by zero.
    """

    value_one = float (input("enter a number:"))
    value_two = float (input("enetr a number:"))

    sum_result = value_one + value_two
    division_result = value_one / value_two
    product_result = value_one * value_two
    difference_result = value_one - value_two

    print(f"The sum of {value_one} and {value_two} is : {sum_result}")
    print(f"The divide of {value_one} and {value_two} is: {division_result}")
    print(f"The Product of {value_one} and {value_two} is : {product_result}")
    print(f"The difference {value_one} and {value_two} is : {difference_result}")

except ValueError:
    print(" Error :Please enter a Valid integars")
except ZeroDivisionError :
    print("Error:Divsion by zero is not Allowed")

