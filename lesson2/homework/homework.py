# Homework Problem 1
# Ask the user for two numbers.
# Print their quoient and remainder on separate lines.
user_input_1=input ("Choose a dividend : ")
user_input_2= input ("Choose a divisor : ")
print (user_input_1)
print (user_input_2) 
quoient= int(user_input_1) // int(user_input_2)
print (quoient)
remainder= int(user_input_1) % int(user_input_2)
print ( remainder)


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal= input("What is your favorite animal? : ")
color= input("What is your favorite color? :")
print ("A " + color + " " + animal + " would be cool")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range (0,11):
    if i % 2 == 0:
        print (i)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
user_input= input ("How much pushups can you do? ")
print (int(user_input) * 7)




# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range (1,6):
    print (i**i)
