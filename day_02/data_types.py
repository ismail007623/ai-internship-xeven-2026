"""Examples of basic data types"""

num1 = 10
num2 = 10.5
is_interview = True
message = "Hi i ma future Ai engineer"

# Values of variable
print(num1)
print(num2)
print(is_interview)
print(message)

# Types of Values
print(type(num1))
print(type(num2))
print(type(is_interview))
print(type(message))

# Type Conversion

int_to_string = str(num1)
str_to_float = float ("12.5")
float_to_int = int (str_to_float)

# Values before conversion and after conversion

print(num1 ,"->", type(int_to_string))
print(message , "->", type(str_to_float))
print(num2 , "->",type(float_to_int))

