# Problem 1
# Use a while loop to print the word "Python" 4 times.
count = 0
while count < 4:
    print("Python")
    count += 1

# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
count = 1
while count < 12: 
    if count % 2 == 0:
        print (count)
    count += 1
    

# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
count = 0
user = int(input("Choose a positive number"))
while count <= user:
    print (count)
    count += 1 

# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
user2 = int(input("Enter a number higher than 10 : "))
count = 0
while user2 > 0:
    print(count)
    user2 -= 5
    count += 1

# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals = ["Shark", "Lion", "Bear"]
index = 0
while index < len(animals):
    print(animals[index] +" is awesome!")
    index += 1
