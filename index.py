# print("Hello... How are doing?")
# print(23 + 1)

# Commenting 
# 1. single line comment
#  2. Multi line or block comment / doc string



# print()
# 1. Buy Data
# 2. Check balance
# 3. Exit



# indentation

# def hello():
    # print('Helloo')


# python variables
# student = "Kingsley"
# balance = 2950.50

# Three Essential component/things we need to know about variable
# 1. variable name
# 2. Assignment operator
# 3. Value
 
# print(balance)
# print(student)

# Rules/Laws guiding variable declaration
# 1. A variable name can only start with underscore or an alphabet
# 2. A variable name can only contain alphabets, number and underscore 
# 3. A variable name doesn't include spaces
# 4. Variable name must be descriptive enough
    
    # i. camel casing.
# firstNameOfTheStudent = "Kingsley"
    # ii. pascal casing.
# FirstNameOfTheStudent = "Kingsley"
    # iii. snake_casing
# first_name_of_the_student = "Kingsley"


# Types of variable declaration 
# 1. Single variable single value
# first_name = "Kingsley"

# 2. Single variable multiple value
# students = "Ayomide", "Olamide", "John"
# print(students)

# 3. Multiple variables single value
# x = y = z = 10
# x = 20
# print(x)

# 4. Multiple variable multiple value
# a, b, c = 10, 20, 30
# print(a)

# Variable Dynamics Functions
# name = input("first_name: ") 
# print(name)


# Concatenation - (Ability to join two or more strings type together)
# print("Hello" + " World")
# first_name = "Kingsley"
# last_name = "Bola"
# age = 20
# account_balance = 5000.5

#Using +
# print("welcome to class "+ first_name)
# print("My name is "+ first_name +" "+ last_name)
# print("I am "+ str(age) + " years old")
# print("Your balance is #"+str(account_balance))

# Using Comma 
# print("welcome to class", first_name)
# print("My name is", first_name, last_name)
# print("I am", age, "years old")

# F-string
# print(f"welcome to class {first_name}")
# print(f"My name is {last_name} {first_name}")
# print(f"I am {age}years old")
# print(f"Your balance is #{account_balance}")


# Variable Dynamics Functions
# first_name = input("first_name: ")
# print(f"welcome to class {first_name}")




#Assignment - Create atlease five variables that tells us about yourself, use them to create a sentence using
# the plus+, comma and F-strings concatenating  approach

# Introduction = "I am a Egbowon Kingsley, passionate Frontend Developer with a strong interest in building responsive and user-friendly web applications."
# Education = "I have experience with HTML, CSS, JavaScript, React, SQL, Excel, and Power BI."
# Technical_skills = "I enjoy solving problems, learning new technologies, and continuously improving my skills."
# Experience = "I work well in teams, communicate effectively, and adapt quickly to new challenges."
# Career_goal = "I am eager to contribute my skills while growing professionally in a dynamic organization."

# print("Assignment for Concatenation")
# print("#Plus ")

# print("Introduction: " + Introduction)
# print("Education: " + Education)
# print("Technical Skills: " + Technical_skills)
# print("Experience: " + Experience)
# print("Career Goal: " + Career_goal)


# print("#Comma ")


# print("Introduction:", Introduction)
# print("Education:", Education)
# print("Technical Skills:", Technical_skills)
# print("Experience:", Experience)
# print("Career Goal:", Career_goal)


# print("#F-string")


# print(f"Introduction: {Introduction}")
# print(f"Education: {Education}")
# print(f"Technical Skills: {Technical_skills}")
# print(f"Experience: {Experience}")
# print(f"Career Goal: {Career_goal}")

# Square bracket []
# Colly braces {}
# Parenthesis ()

# PYTHON DATATYPES
# 1. Text Type / strings. It is denoted by "" or ''. str()Is the object name for strings
# name = "Ayomide"
# print(type(name))

# 2. Number types
    # i. Integers - int() e.g 12, 230  (whole numbers)
    # ii. Float - float() e.g 1.5, 23.455
    # iii. Complex - complex() e.g 2 + 3j

# num = 10
# print(type(num))

# 3. Sequence type 
    # i. tuple - (1, 3, 5, 6)  - () Parenthesis 
    # ii. list - [1, 3, 5, 6]  - [] Square Bracket
    # iii. range - range()  Will as you for the (Start, Stop(the only compulsory one), and Step)

# numbers = (1, 3, 5, 6)
# numbers = (1, 3, 5, 6)

# numbers = range(10)

# print(type(numbers))
# print(numbers)
# To convert list to numbers, To convert tuple to numbers
# print(list(numbers))
# print(tuple(numbers))

# 4. Boolean type - False(0), True(1)  The class name of Boolean is BOOL

# isEducated = True
# print(type(IsEducated))

# print(int(isEducated))

# 5. Set Type - set() - {1, 3, 5, 6}
# numbers = {1, 3, 5, 6, 2, 4}
# students = {"Ayomide", "Olamide", "John"}
# print(type(numbers))
# print(numbers)

# 6. mapping type are called(dictionary) - dict()   It works as key and value{"name": "Ayo", "age": 20}
# student = {"name": "Ayo","age": 20}
# "isActive": True

# print(type(student))
# print(student["name"])

# 7. None type 
# box = None
# print(type[box])

#. 8. Binary Types : Byte, bytearray, memoryview


# num = "12"
# print(str(num))

# amount = float(input('amount: '))
# print(type(amount)) 



# PYTHON OPERATORS

# 1. Arithmetic operator: +, -, /, *, **(exponential/raise to power), //(floor division meaning return the whole number), 
# %(modulus it means divide 5 by 2 the result is "return the remainder" and if there's no remainder return 0)
# print(5 ** 2)
# print(5 // 2)
# print(5 % 2)

# 2. Assignment operator(To asign values to a variables): =, +=, -=, /=, %=, //=  e.t.c
# x = 5
# x += 2 #x = x + 2
# x -= 2

# print(x)

# 3. Comparision operator: == (equal to), !=(not equal to), >, <, >=, <=
# x = 5
# print(x == 5)


# 4. Logical operator: AND (The two condition must be true before i have true), OR (One condition must be true for me to be true), 
# NOT(Negate the value of A)

"""
A ---- B --- AND --- OR ---- XOR
0      0      0       0       0
0      1      0       1       1
1      0      0       1       1
1      1      1       1       0

NOT A (Negate the value of A)
1
1
0
0

"""

# age = 20
# paymentStatus = True
# print(age >18 or paymentStatus)
# print(not paymentStatus)

# email_is_verified = True
# password_is_verified = False
# print(email_is_verified and password_is_verified)


# CONDITIONAL STATEMENT (if/else/elif)   elif(It's used for Multiple condition)

# x = 3 

# if x ==3:
    # print('yes! ')
# else:
    # print("Oh no !")

# if email_is_verified:
    # print("Access Granted.")
# else: 
    # print("what you are looking for")

# if email_is_verified and password_is_verified:
    # print("Login Successful")
# else:
    # print("Incorrrect email or password")

# original = 3
# predicted_score = int(input("Predicted score: "))

# if predicted_score == original:
    # print('You won 100k')

# elif predicted_score > 2:
    # print('You tried, you won 10k')

# else:
    # print("Sorry oh!" you get nothing)

# fizz - divisble by 3 with no remainder
# Buzz - divisble by 5 with no remainder
# fizzBuzz - divisble by 3 and 5 with no remainder


# number = int(input("Number: "))

# if number % 3 == 0 and number % 5 == 0:
    # print(f"{number} is a FizzBuzz")

# elif number % 3 == 0:
    # print(f"{number} is a Fizz")

# elif number % 5 == 0:
    # print(f"{number} is a Buzz")

# else: 
    # print(f"{number} is neither Fizz nor Buzz")


# Classwork

# Build a system that tells if a number is odd or even


# number = int(input("Enter a number: "))

# if number % 2 == 0:
    # print(f"{number} is Even")
# elif number % 2 != 0:
    # print(f"{number} is Odd")
# else:
    # print("Something went wrong")



# 5. Identity operator(checking between two variables): is, is not
# x = 5 
# print(x == 5) Is a question saying x is 5
# y = 5

# print(x is not y)

# 6. Membership operator: in, not in
# students = ["Kingsley", "Moni", "Kelly"]
# student = 'Goke'

# print(student in students)
# print(student not in students)


# 7. Bitwise operator(use with binary number): 
# $ -> AND
# | -> OR (One condition must be true for me to be true)
# ~ -> NOT
# ^ -> XOR (exclusive or) Only one condition must be true for me to be true

# val1 = 20
# val2 = 10
# print(bin(val1))
# print(bin(val2))

# print(val1 & val2)

# x = 10
# y = 5
# print(bin(x))
# print(bin(y))
# print(bin(x & y))

"""
1  0  1  0
&  1  0  1

"""


# x = 10
y = 5
# print(~x)
# print(bin(y))
# print(bin(x ^ y))

"""
1  0  1  0
   1  0  1
1  1  1  1

"""

# A simple email validator
# email = input("Email: ")

# if '@' in email and '.' in email:
    # print(f"(email) is valid email. ")

# else:
    # print("Invalid email")

# PYTHON STRINGS 

# name  = 'Ayo' # ['A', 'y', 'o']

# print(ord('a'))
# print(name[-1])
# print(len(name))

# exp = "Hi Everyone, Python is my favorite programming language."
# exp = "(The spaces here is called leading white spaces)  Hi Everyone, Python is my favorite programming language. The spaces here is called trailing white spaces"

# print(len(exp))
# print(exp[3:11])
# print(exp[3:])

# print(exp.upper())
# print(exp.lower())
# print(exp.capitalize())
# print(exp.title())

# print(len(exp.strip()))

# action = input("Are you sure? Yes/No: ")
# if action.strip().lower() == 'yes':
    # print('Proceed')

# else:
    # print('Decline')


# 1. Build a simple grading system
# 70 - 100  = A
# 60 - 69 = B
# 50 - 59 = C
# 45 - 49 = D
# 40 - 44 = E
# 0 - 39 = F


# 2. Build a simple CBT app. 

# score = int(input("Enter your score: "))

# if score >= 70 and score <= 100:
    # print("Grade: A")
# elif score >= 60 and score <= 69:
    # print("Grade: B")
# elif score >= 50 and score <= 59:
    # print("Grade: C")
# elif score >= 45 and score <= 49:
    # print("Grade: D")
# elif score >= 40 and score <= 44:
    # print("Grade: E")
# elif score >= 0 and score <= 39:
    # print("Grade: F")


CBT_APP = "WELCOME TO THE ENGLISH CBT QUIZ"
Instruction = "Read the questions carefully and pick the correct answers from the options"
score = 0

q1 = "Choose the word closest in meaning to 'diligent.' \na. Lazy b. Hardworking c. Careless d. Weak"
print(q1)
answer = input("answer: ").strip()
if answer.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Wrong!")



"""
Question_One = {
"Question": "Choose the word closest in meaning to 'diligent.'",
"Options": {
    "A": "Lazy",
    "B": "Hardworking",
    "C": "Careless",
    "D": "Weak"
},
"Answer": "B"
}
Question_Two = {
"Question": "Choose the word opposite in meaning to 'ancient.'",
"Options": {
    "A": "Old",
    "B": "Historic",
    "C": "Modern",
    "D": "Traditional"
},
"Answer": "C"
}

Question_Three = {
"Question": "Which of the following is grammatically correct?",
"Options": {
    "A": "She have gone to school",
    "B": "She has gone to school",
    "C": "She having gone to school",
    "D": "She have went to school"
},
"Answer": "B"
}

Question_Four = {
"Question": "Identify the noun in the sentence: 'The teacher explained the lesson.'",
"Options": {
    "A": "Explained",
    "B": "The",
    "C": "Teacher",
    "D": "Lesson"
},
"Answer": "C"
}

Question_Five = {
"Question": "Choose the correct plural form of 'criterion.'",
"Options": {
    "A": "Criterions",
    "B": "Criteria",
    "C": "Criterias",
    "D": "Criteriones"
},
"Answer": "B"
}

Question_Six = {
"Question": "Complete the sentence: 'If I had known, I _____ earlier.'",
"Option": {
    "A": "Will come",
    "B": "Would come",
    "C": "Would have come",
    "D": "Will have come",
},
"Answer": "C"
}

Question_Seven = {
"Question": "Which word is correctly spelled?",
"Options": {
    "A": "Accomodation",
    "B": "Acommodation",
    "C": "Accommodation",
    "D": "Accommmodation",
},
"Answer": "C"
}

Question_Eight = {
"Question": "Choose the correct preposition: 'She is good _____ Mathematics.'",
"Option": {
    "A": "In",
    "B": "On",
    "C": "At",
    "D": "With"
},
"Answer": "C"
}

Question_Nine = {
"Question": "What is the meaning of 'procrastinate'?",
"Option": {
    "A": "To work quickly",
    "B": "To postpone something",
    "C": "To complete something",
    "D": "To explain something",
},
"Answer": "B"
}

Question_Ten = {
"Question": "Choose the correct sentence.",
"Options": {
    "A": "Neither John nor James are present",
    "B": "Neither John nor James is present",
    "C": "Neither John or James is present",
    "D": "Neither John or James are present",
    },
    "Answer": "B"
}
print(Instruction)

# "Answers and Score"

print(Question_One)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_One["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)


print(Question_Two)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Two["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Three)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Three["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Four)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Four["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Five)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Five["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Six)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Six["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Seven)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Seven["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Eight)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Eight["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Nine)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_Nine["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

print(Question_Ten)
user_answer = input("Enter your answer: (A, B, C, D): ")
if user_answer.upper() == Question_One["Answer"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your score is:", score)

"""



# Python Collections or Array
# 1. List: It can be indexed, changeable, allows duplicate items, ordered 
# [] or list{}
# basket = ['Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish']
# print(type(basket))
# print(basket[-1])
# print(basket[0:4])
# basket[3] = 'Egg'


# basket.append('Egg') Meaning we want to add to the list
# basket.insert(3, 'Egg')
# basket.extend("Egg", 'Oil')  (It only accept multiple values)
# basket.pop(0)
# basket.remove('Meat')
# basket.clear()

# print(basket.index('Fish', 4))
# print(basket.count('Fish'))

# basket.sort(key=str.lower, reverse=True)
# print(basket)

# scores = [12, 14, 16]
# print(sum(scores))
# print(max(scores))


# 2. tuple: indexed, allows duplicate, ordered, unchangeable
# () or tuple()

# basket = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# print(type(basket))

# print(basket[0])
# basket[0] = "Apple"

# print(basket.count("Fish"))
# print(basket.index("Meat"))

# new_basket = list(basket)
# print(new_basket)
# new_basket[0] = "Apple"
# basket = tuple(new_basket) 
# print(basket)

# unpacking

# a, b, c, d, e, f = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# a, b, *c, f = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# *a, b = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')

# *a, = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# print(a)


# 3. set: unordered, doesn't allow duplicate, unchangeable, can't be indexed (It's direct opposite of List)
# {} or set()

# basket = {'Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish'}
# print(basket[0])
# basket[0] = "Apple"

# basket.add('Apple')
# basket.update(["Apple", "Egg"])
# basket.pop()
# basket.remove('Fisherman')
# basket.discard('Fisherman')
# print(basket)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {2, 4, 10, 12, 11}
# setC = {1, 2, 3, 4}

# print(setA.union(setB))
# print(setA.intersection(setB)) (what is common inbetween the two sets and what can i use to join the two set that's 2 and 4)
# print(setA.difference(setB))
# print(setB.difference(setA)) 
# print(setA.symmetric_difference(setB)) (difference across the two sets)

# setA.symmetric_difference_update(setB)
# print(setA)

# print(setA.issubset(setC))   (It will give a Boolean result True/False)


# 4. dictionary 
# {key:value} or dict()

"""
car = {
    "brand": "Toyota",
    "model": "Camry 2026",
    "color": "wine",
    "type": "hybrid",
    "owner": {
     "name": "Monioluwa",
         "address": {
             "state": "Oyo state",
             "country": "Nigeria"
         }
     }
}

"""


# print(car['types'])
# print(car['owner']['address']['country'])
# owner = car['owner']
# print(owner['address']['country'])

# print(car.keys())
# print(car.values())
# print(car.items())

# print(car.get('type', "Not Found"))
# car.pop('type')
# car.popitem()

# car.update({"model": "Camry 2027"})
# car['model'] = "Camry 2027"

# print(car)


# Python Loop
# 1. For loop: it iterate over a sequence(e.g list, tuple, set, or string)

# name = "Monioluwa"
# for x in name:
#     print(x)
#     print("_______")

# students = ["Ade", "John", "Ola"]
# for student in students:
#     print(f"Welcome to class {student}")


# score = 0
questions = [
    "What is the capital of Lagos a. Ikeja b. Iyanapaja",
    "What is the capital of Edo a. Ikeja b. Benin",
    "What is the capital of Osun a. Osogbo b. Iyanapaja",
]
answers = ["a", "b", "a"]
marks = [10, 20, 5]

# x = 1

# for ques, ans, mark in zip(questions, answers, marks):
#     print(f"{x}. {ques}")
#     x+=1

#     # marking scheme
#     user_ans = input("Ans: ")
#     if user_ans.strip().lower() == ans:
#         print("Correct")
#         score += mark
#     else:
#         print("Incorrect")

# print(f"Total score: {score}/{sum(marks)}")



# exam = [
#     ("What is the capital of Lagos a. Ikeja b. Iyanapaja", "a", 10),
#     ("What is the capital of Edo a. Ikeja b. Benin", "b", 20),
#     ("What is the capital of Osun a. Osogbo b. Iyanapaja", "a", 5)
# ]


# # a, b, c=("What is the capital of Lagos a. Ikeja b. Iyanapaja", "a", 10)

# no = 1
# for ques, ans, mark in exam:
#     print(f"{no}. {ques}")
#     no+=1

#     user_ans = input("Ans: ")
#     if user_ans.strip().lower() == ans:
#         print("Correct")
#         score += mark
#     else:
#         print("Incorrect")

# print(f"Total score: {score}/{sum(marks)}")


# exam = {
#     "What is the capital of Lagos a. Ikeja b. Iyanapaja": "a",
#     "What is the capital of Edo a. Ikeja b. Benin": "b",
#     "What is the capital of Osun a. Osogbo b. Iyanapaja": "a"
# }

# print(exam.items())

# for ques, ans in exam.items():
#     print(ans)


# students = ["Ade", "John", "Ola"]
# for student in students:
#     print(student)  
#     for letter in student:
#         print(letter)


# for x in range(1, 6):
#     print(f"{x} Times Table")
#     for y in range(1, 6):
#         print(f"{x} x {y} = {x*y}")



# 2. While loop: While keeps iterating as long the condition is True.

# x = 10
# while x > 0:
#     print(x)
#     x -= 1


# balance = 1000
# while balance > 100:
#     balance -= 100
#     print("You can still buy stuff, balance is", balance)

#     if balance == 500:
#         print("I no dey buy again")
#         break



# ticket = 10
# while ticket > 0:
#     age = int(input("Age: "))
#     if age < 18:
#         print("Access not granted")
#         continue

#     ticket -= 1
#     print("Ticket remains", ticket)

x = 10

# while True:
#     x -= 1
#     print(x)
#     if x == 4:
#         break


# A simple Todo app

database=[]
# database=[]

while True:
    print("""
    1. Add a todo
    2. Delete a todo
    3. Edit a todo
    4. View all
    5. Clear all
    6. Set todo as completed
    #. exit
    """)
    choice = input("Choice: ").strip()
    if choice == '1':
        print('Add Todo')
        todo = input("Your Todo: ").strip().capitalize()
        if todo:
            database.append(todo)
            print("Todo saved.")
        else:
            print("No todo added.")
# while True:
#     print("""
#     1. Add a todo
#     2. Delete a todo
#     3. Edit a todo
#     4. View all
#     5. Clear all
#     6. Set todo as completed
#     #. exit
#     """)
#     choice = input("Choice: ").strip()
#     if choice == '1':
#         print('Add Todo')
#         todo = input("Your Todo: ").strip().capitalize()
#         if todo:
#             database.append(todo)
#             print("Todo saved.")
#         else:
#             print("No todo added.")

    elif choice == "2":
        print("Delete Todo")
        item_no = int(input("Delete Item no: "))
#     elif choice == "2":
#         print("Delete Todo")
#         item_no = int(input("Delete Item no: "))

        if item_no > len(database):
            print("Invalid Item no. Try again.")
            continue
#         if item_no > len(database):
#             print("Invalid Item no. Try again.")
#             continue

        index = item_no - 1
        database.pop(index)
        print("Todo Deleted.")
#         index = item_no - 1
#         database.pop(index)
#         print("Todo Deleted.")


    elif choice == "3":
        print("Edit Todo")
        item_no = int(input("Edit Item no: "))
#     elif choice == "3":
#         print("Edit Todo")
#         item_no = int(input("Edit Item no: "))

        if item_no > len(database):
            print("Invalid Item no. Try again.")
            continue
#         if item_no > len(database):
#             print("Invalid Item no. Try again.")
#             continue


        new_name = input("New: ").strip().capitalize()
        if not new_name:
            print("Todo can't be empty")
            continue
#         new_name = input("New: ").strip().capitalize()
#         if not new_name:
#             print("Todo can't be empty")
#             continue

        index = item_no - 1
        database[index] = new_name
        print("Todo edited successfully")
#         index = item_no - 1
#         database[index] = new_name
#         print("Todo edited successfully")



    elif choice == "4":
        print("View all Todo")
#     elif choice == "4":
#         print("View all Todo")

        no = 1
        for todo in database:
            print(f"{no}. {todo}")
            no+=1
#         no = 1
#         for todo in database:
#             print(f"{no}. {todo}")
#             no+=1

    elif choice == "5":
        print("Clear all Todo")
#     elif choice == "5":
#         print("Clear all Todo")

        database.clear()
#         database.clear()


    elif choice == "#":
        # exit("Goodbye!")
        break
#     elif choice == "#":
#         # exit("Goodbye!")
#         break

    else:
        print("Invalid input")
#     else:
#         print("Invalid input")



    
[
    {
        "todo": "Eat",
        "completed": False
    }
]

# .pop , .append, .update, .extend


# value1= float(input("Value 1: "))
# value2= float(input("Value 2: "))

# print("""
#     1. Addition
#     2. Subtraction
#     3. Division
#     #. Exit     
# """)

# choice = input("choice: ").strip()
# if choice == "1":
#     print(f"Ans: {value1 + value2}")
# elif choice == "2":
#     print(f"Ans: {value1 - value2}")
# elif choice == "3":
#     print(f"Ans: {value1 / value2}")
# elif choice == "#":
#     exit('Goodbye !')
# else:
#     print("Invalid option")


# ussd app - conditional statement
# simple banking system - conditional statement, operators, data structure
# bet app - set, conditional, loop


# deposit, withdraw, create account, login, check balance, 


database = []

while True:
    print("""
        1. Create Account
        2. Login
        #. Exit      
    """)
    
    choice = input("Choice: ").strip()
    if choice == "1":
        fullname = input("Fullname: ").strip().title()
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()
       
        if not fullname or not email or not password or not confirm_password:
            print("❌All fields are required")
            continue
        
        if password != confirm_password:
            print("❌Password doesn't match")
            continue
        
        user = {
            "fullname": fullname,
            "email": email,
            "password": password,
            "balance": 0.0
        }
        database.append(user)
        print("Registration successfull") 
           
       
    elif choice == "2":
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        active_user = None
        
        
        for user in database: # [{}, {}, {}]
            if user['email'] == email:
                active_user = user 
        
        if not active_user or active_user['password'] != password:
            print("Invalid email or password")
        else:
            print("Login successfull")
            while True:
                print("""
                1. Deposit
                2. Withdraw
                3. Check balance
                #. Logout   
                """)
                
                choice = input("Choice: ").strip()
                if choice == "1":
                    # print(active_user)
                    amount = float(input("Amount: "))
                    if amount < 1:
                        print("Amount can't be less and #1.")
                        continue
                    
                    active_user['balance'] += amount
                    print(f"You've deposited #{amount}. Your account balance is #{active_user['balance']}")
                    
                    # print(database)
                    
                elif choice == "2":
                    amount = float(input("Amount: "))
                    if amount < 1:
                        print("Amount can't be less and #1.")
                        continue
                    
                    if amount > active_user['balance']:
                        print("Insufficient funds")
                        continue
                    
                    active_user['balance'] -= amount
                    print(f"You've withrawn #{amount}. Your account balance is #{active_user['balance']}")
                    
                elif choice == "3":
                    print(f"Your account balance is #{active_user['balance']}")
                elif choice == "#":
                    print("Signing out...")
                    break
                else:
                    print("Invalid choice.")
        
    elif choice == "#":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")