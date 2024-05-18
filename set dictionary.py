#way to build SET = {}
x_1={1, 4, "3",3,4}  #output only show one 4, not repeat
print(x_1)

username=["user1","user2","user3"]
age=[21,23,24]
information={"Topic1":username,
             "Topic2":age
             }
print(information["Topic1"])

student = {
    "name": "Alice",
    "age": int(20),
    "major": "Computer Science",
    "grades": {
        "math": 95,
        "english": 88,
        "history": 92
    }
}

# Access dictionary values by keys
student_name = student["name"]
student_age = student["age"]

# Modify dictionary values
student["age"] = 21
student["grades"]["math"] = 97

# Add a new key-value pair
student["gender"] = "Female"

# Check if a key exists in the dictionary
has_major = "major" in student
has_height = "height" in student
print ("has major =",has_major)
# Get the list of keys and values
keys = student.keys() 
values = student.values()

# Iterate through the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key-value pair
del student["grades"]

# Print the updated dictionary
print("\nStudent Information after removing 'grades':")
for key, value in student.items():
    print(f"{key}: {value}")