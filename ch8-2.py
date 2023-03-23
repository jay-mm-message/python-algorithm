phone_book = {}
phone_book['Trump'] = '0911111111'
phone_book['Ellen'] = '0922222222'
phone_book['Tom'] = '0933333333'
phone_book['Ellie'] = '0944444444'

name = input("Entry phone book names: ")
if name in phone_book:
  print("{}'s phone number is {}".format(name, phone_book[name]))
else:
  print("{} This name is not in phone book".format(name))