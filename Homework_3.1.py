the_string= input('Enter your sentence :')
length_of_sentence = len(the_string)
centre = length_of_sentence // 2
first_symbol = centre -1
last_symbol = first_symbol +3
centre_3_symbols = the_string[first_symbol:last_symbol]
if length_of_sentence < 7:
    print(False)
else:
    print (centre_3_symbols)
