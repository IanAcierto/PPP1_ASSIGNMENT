def hello(user):
  print("Hello " + user)

def pack(arg1, arg2, arg3):
  return [arg1, arg2, arg3]

def eat_lunch(lunch_items):
  if len(lunch_items) == 0:
    print("no lunch")
  else:
    for i in range(len(lunch_items)):
      if i == 0:
        print("First i eat " + lunch_items[i])
      else: print("then i eat " + lunch_items[i])
    