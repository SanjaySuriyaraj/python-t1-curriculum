# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input= input ("Enter a number : ")
if (int(user_input) % 2 == 0):
    print ("Even")
else:
    print ("Odd")  


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
user_input= input ("what day of the week is it? :")
if (str(user_input)) == ("saturday" or "sunday") :
    print ("weekend")
else:
    print ("weekday")



# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
num = random.randint (1, 11)
user_input= input ("Guess a number between one to ten : ")
if int(user_input) ==  num:
    print ("Correct")
else:
    print ("Try Again")
print("The random generated number is : " + str(num) )


# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
user_input= input ("Say a random positive number: ")
if (int(user_input)%2 == 0) and (int(user_input) > 10) :
    print ("Big even number")
else:
    print ("Number does not meet criteria")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
user_input= input ("Say one number : ")
user_input2= input ("Say another number : ")
user_input = int(user_input)
user_input2 = int(user_input2)
if user_input == user_input2:
    print ("Numbers are equal")
elif user_input > user_input2:
    print ("The bigger number is : " + str(user_input))
else:
    print("The bigger number is : " + str(user_input2))
