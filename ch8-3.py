voted = {'Trump': None, 'Ellie': None, 'Ellen': True, 'Tom': None}

def check_name(name):
  if voted[name]:
    print("You have already voted")
  else:
    print("Welcome a voter")
    voted[name] = True

name = input("Please enter your name: ")

if name in voted:
  check_name(name)
else:
  print("You are not a voter")