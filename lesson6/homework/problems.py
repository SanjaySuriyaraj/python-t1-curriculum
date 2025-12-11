# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names)
num_alex= names.count("Alex")
print (num_alex)



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
if "elephant" in animals:
    print ("Found elephant")
else:
    print ("No elephant found")    


# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
num_score= scores.count (100)
print (num_score)


# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
if "blue" in colors:
    print ("Found blue")
    print (colors.index("blue"))
else:
    print ("Blue not found")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
counter = 0
for i in range (len(temperatures)) :
    item= temperatures[i]
    if item  < 0 :
        counter = counter + 1
print ("temperatures below 0 : ", counter )
