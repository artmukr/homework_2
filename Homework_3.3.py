number = int(input('enter your number :'))
number = str(number)
number_1 = number[::-1]
if number == number_1:
    print(True)
else:
    print(False)
