# Define a string variable
message = "Hello, World!"

# Print the string
print(message)

# Access individual characters in the string
fifth_character = message[5]
print("The fifth character is:", fifth_character)

# Find the length of the string
length = len(message)
print("The length of the string is:", length)

#
# Get user input for the name
hobby = input("Enter your hobby: ")
#
#

# Concatenate (combine) two strings
greeting = "Hello,your hobby is " + hobby + "!"
print(greeting)

# Use string methods
uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_DuniA = "DuniA" in greeting
print("Does the message contain 'DuniA'? ", contains_DuniA)

# Replace part of the string
new_message = message.replace("DuniA", "World")
print("Updated message:", new_message)