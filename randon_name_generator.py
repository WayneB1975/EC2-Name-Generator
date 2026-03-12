import random

#Define Letters and Numbers Manually
letters = "ABCDEFG"
numbers = "1234567"

#Combine Letters and Numbers Into One Pool of Characters
characters = letters + numbers

#Approved Departments
approved_departments = ["marketing", "accounting", "finops"]

#Function to Generate a Random String
def generate_random_string (length):
    random_result = ""
    for _ in range (length):
        random_character = random.choice(characters)
        random_result = random_result + random_character
    return random_result

#Get User Input
num_instances = int(input('How many EC2 instance names do you need?:\n'))
name_department = input("Enter your department's name:\n")


#Check if Department is Approved 
if name_department.lower() in approved_departments:
    for _ in range(num_instances):
        print(name_department + "-" + generate_random_string(6))
else:
    print("Your Department is not authorized to use this Name Generator")