try :
    students = ['Ali','jhon','jason','shery','moiez']
    print(type(students))
    print(students)
    students.insert(5,'irfan')
    students.append('honey')
    print(students)
    students.remove('Ali')
    print(students)
    students.pop(3)
    print(students)
    first_three_students = students[:3]
    print(first_three_students)
    students.sort()
    print(students)
except IndexError:
    print("Wrong index")
except TypeError :
    print("Worng data type")