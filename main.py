Calcu = ["(M)ultiplication", "(D)ivision", "(A)ddition", "(S)ubtraction"]
print(Calcu)
Calc = input("What operation do you want to use: ")

if Calc.upper() == "M":
  num = float(input("First Number: "))
  num1 = float(input("Second Number: "))
  print(num*num1)
elif Calc.upper() == "D":
  num = float(input("First Number: "))
  num1 = float(input("Second Number: "))
  print(num/num1)
elif Calc.upper() == "S":
  num = float(input("First Number: "))
  num1 = float(input("Second Number: "))
  print(num-num1)
elif Calc.upper() == "A":
  num = float(input("First Number: "))
  num1 = float(input("Second Number: "))
  print(num+num1)
else:
  print("This is not a supported operator")