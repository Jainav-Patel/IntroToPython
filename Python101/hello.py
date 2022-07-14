# Ask user for their name
name = input("what's your name? ").strip().title()

#Remove whitespaces from str that is inputted by users and capitalizes user's name
#name = name.strip().title()

#Capitalize user's name (only capitalize's first letter of first word)
# name = name.capitalize()

# Capitalize user's name (capitalize's first letter of every word!)
#name = name.title()

#Say hello to user in different ways
print("hello " + name)
print("hello ", end="")
print(name)
print ("hello ", name, sep="???")
print(f"hello {name}")