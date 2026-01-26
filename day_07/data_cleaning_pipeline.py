messy_data = ['apple',   None,  ' apple ','Apple',None , 'cherry',   'alo' ,'banana','  Banana   ']

print("List with messy data:",messy_data)

# step 1 removing None values
step_1 = [i for i in messy_data if i is not None]

print("Removed none value form List:",step_1)

# step 2 List after lower case
step_2 = [i.lower() for i in step_1]

print("list after lower case :" , step_2)

# step 3 After removing white spaces
step_3 = [i.strip() for i in step_2]

print("After removing white spaces :",step_3)

# step 4 Removing duplicate
step_4 = [i for i in set(step_3)]

print("Removed duplicate:",step_4)


print("\nList before with mess data :",messy_data)
print("List after removed None value duplicates white space , normalize:",step_4)