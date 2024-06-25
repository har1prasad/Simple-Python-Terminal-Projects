end_of_program = False

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

fn = int(input("Enter the first number ?: "))

while not end_of_program:
  op = input("Enter the operator ['+' '-' '*' '-']: ")
  sn = int(input("Enter the second number ?: "))

  if op == '+':
      tm = add(fn, sn)
      print(f"{fn} + {sn} = {tm}")
  elif op == '-':
      tm = sub(fn, sn)
      print(f"{fn} - {sn} = {tm}")
  elif op == '/':
      tm = div(fn, sn)
      print(f"{fn} / {sn} = {tm}")
  elif op == '*':
      tm = mul(fn, sn)
      print(f"{fn} * {sn} = {tm}")
  else:
      print("invalid operator choosed")

  end_of_choice = False
  while not end_of_choice:
    con = input("Do you want to continue calculation 'Y' or 'N': ").lower()
    if con == "y":
        fn = tm
        end_of_program = False
        end_of_choice = True
    elif con == "n":
        end_of_program = True
        end_of_choice = True
    else:
        print("invalid choice")
        end_of_choice = False