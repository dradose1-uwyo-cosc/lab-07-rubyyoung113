# Ruby Young 
# UWYO COSC 1010
# 11/6/24
# Lab 07
# Lab Section: 16
# Sources, people worked with, help given to: Nile Young 


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered


factorial = 1

while True:
    upper_bound = input("Enter a positive number to find the factorial: ")
    if upper_bound.isdigit():
        break
    else:
        print('Enter only a positive number please!')

number = 1 
upper_bound = int(upper_bound)
while number <= upper_bound:
    factorial *= number
    number += 1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

total_sum = 0 
pos_int = 0
neg_int = 0 
while True: 
    integers = input("Enter an integer value to sum them, (to stop enter exit): ")

    if integers.lower() == 'exit':
        print("You have exited the loop :)")
        break 
    elif integers[0] == '-':
        integers = integers.replace("-","")
        neg_int += int(integers)
    elif integers.isnumeric():
        pos_int += int(integers)
    else:
        print("Enter an integer or 'exit' to end the loop and get your result")
    
total_sum = pos_int - neg_int
print(f"The total sum of the integers is {total_sum}")


print('*'*75)

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 


number1 = 0
symbol = 0
number2 = 0
answer = 0

while True:
    equation = input("Input a operan operater operand equation (or enter exit to stop): ")
    equation = equation.replace(" ","") #removes the spaces in the equation 

    if equation.lower()== 'exit':
        print("You have exited the loop :)")
        break
    if '+' in equation:
        symbol = '+'
    elif '-' in equation:
        symbol = '-'
    elif '*' in equation:
        symbol = '*'
    elif '/' in equation:
        symbol = '/'
    elif '%' in equation:
        symbol = '%'
    else: 
        print("Invalid equation, please enter a valid symbol")
        continue

    parts = equation.split(symbol)

    if len(parts) == 2: 
        number1 = parts[0]
        number2 = parts[1]

    
        if number1.isdigit() and number2.isdigit():
            number1 = float(number1)
            number2 = float(number2)
        

            if symbol == '-':
                answer = number1 - number2
            elif symbol == '+':
                answer = number1 + number2
            elif symbol == '/':
                if number2 == 0: 
                    print("ERROR!(division by zero)")
                    continue
                answer = number1 / number2
            elif symbol == '*':
                answer = number1 * number2
            elif symbol == '%':
                answer = number1 % number2
             
            print(f"The results from the equation is: {answer}")
        else: 
            print(f"Enter only valid operands (positive integers) please or 'exit'")
    else:
        print("Invalid equation format, please enter only in the form: operand operator operand. ")
 