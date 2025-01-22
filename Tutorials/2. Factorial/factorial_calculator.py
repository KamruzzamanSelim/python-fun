while True:
    number = int(input("Enter Your Number: "))
    if number <= 0:  # Check if the number is less than or equal to zero
        print("Bye")
        break  # Exit the loop
    elif number == 1:  # Check if the number is 1
        print("Your Factorial is: 1")
    else:  # Calculate factorial for numbers greater than 1
        product = 1
        for i in range(1, number + 1):
            product *= i
        print("Your Factorial is:", product)
