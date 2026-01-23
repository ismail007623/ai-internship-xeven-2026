try:
    record = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    print(record)
    first_five_element = record [0:5]
    print("First five element in List :"  , first_five_element)
    last_five_element = record[-5:]
    print("Last five element :" ,last_five_element)
    reversed_list = record[::-1]
    print("Reversed list :" , reversed_list)
    every_third_element = record[::3]
    print("Every third element in List :",every_third_element)
    middle_ten_elements = record[5:15]
    print("Ten middle elements :",middle_ten_elements)

except IndexError:
    print("Wrong index")
except TypeError:
    print("Wrong data type")