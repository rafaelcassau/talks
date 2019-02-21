from integer import Integer

first_number = int(input('Type a first integer number: '))
second_number = int(input('Type a second integer number: '))

print('1 - Add')
print('2 - Subtract')
print('3 - Multiply')
print('4 - Divide')
operation = int(input('Type a valid operation! please!: '))

if operation is 1:
    result = Integer(first_number) + Integer(second_number)
    print(result)
elif operation is 2:
    result = Integer(first_number) - Integer(second_number)
    print(result)
elif operation is 3:
    result = Integer(first_number) * Integer(second_number)
    print(result)
elif operation is 4:
    result = Integer(first_number) / Integer(second_number)
    print(result)
else:
    print('Onvalid choice!')



