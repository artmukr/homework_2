string = input('Write the string :')
number = int(input('Write the number of extra letter :'))
ant = number + 1
first_part = string[:number]
second_part = string[ant:]
result = f"{first_part}{second_part}"
print(result)
