import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_system = ["Windows","MacOS","Linux"]   # operating_system[0] = "windows"
print(operating_system[len(operating_system)-1])

operating_system.reverse()
print (operating_system)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
school_subjects= ["Math","English","Social Studies","Science"]
print (school_subjects[1])

school_subjects.sort()
print(school_subjects)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
codes=["401", "402", "403", "404", "405"]
print (len(codes))
print(codes.index("403"))


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
lang= ["Python", "C++"]
print (lang[(random.randint(0, len(lang)-1))])
lang.append ("lua")
print (lang)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords= ["abc","def","ghi","jkl","mno","pqr"]
print (passwords[len(passwords)//2])
passwords.pop(0)
print (passwords)
