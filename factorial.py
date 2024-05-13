#How to calculate factorial of a number
while True:
  number = int(input("Enter Your Number:"))
  if number<=0:  #Check if the number is less than or equal zero, If yes, then print
    print("Bye")
  elif number==1: #Check if the number is equal 1. Then print the factorial 1
    print("Your Factorial is: 1")
  else:  #If the number is greater than 1 then calcualte factorial
    product = number
  while number>1:
    i = number
    product = product*(i-1)
    number = number-1
    if number==1:
        print("Your Factorial is: ",product)
