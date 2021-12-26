repeat = True 
#while loop is like an if statement but when the loops goes to the end it checks the condition and goes back to the top if it is true
while(repeat == True): 
  num1 = int(input('Enter first number ') )
  num2 = int(input('Enter second number ') )
  operation = input('Enter Operation here ')

  #double == is asking a question if two are equal
  if operation == "+" or "add" in operation.lower():
    print(num1 + num2)

  elif operation == "-" or "sub" in operation.lower():
    print(num1 - num2)

  elif operation == "*" or "multi" in operation.lower():
    print(num1 * num2)

  elif operation == "/" or "div" in operation.lower():
    print(num1 / num2)

  else:
    print("Nonsupported")

  temp = input('Do you want to continue ') 
  if not temp == "yes": 
    repeat = False 

