
print("WELCOME TO THE ENGLISH CBT QUIZ")
print("Read the questions carefully and pick the correct answer from the options\n")
score = 0

Q1 = "1. Choose the word closest in meaning to 'diligent.' \nA. Lazy B. Hardworking C. Careless D. Weak"
print(Q1)
answer = input("answer: ").strip()
if answer.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q2 = "2. Choose the word opposite in meaning to 'ancient.' \nA. Old B. Historic C. Modern D. Traditional"

print(Q2)
answer = input("answer: ").strip()
if answer.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q3 = "3. Which of the following is grammatically correct? \nA. She have gone to school. B. She has gone to school.C. She having gone to school. D. She have went to school."

print(Q3)
answer = input("answer: ").strip()
if answer.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q4 = "4. Identify the noun in the sentence: 'The teacher explained the lesson.' \nA. Explained B. The C. Teacher D. Lesson"

print(Q4)
answer = input("answer: ").strip()
if answer.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q5 = "5. Choose the correct plural form of “criterion.” \nA. Criterions B. Criteria C. Criterias D. Criteriones"
print(Q5)
answer = input("answer: ").strip()
if answer.lower() == "5":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q6 = "6. Complete the sentence: “If I had known, I _____ earlier.” \nA. will come B. would come C. would have come D. will have come"
print(Q6)
answer = input("answer: ").strip()
if answer.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q7 = "7. Which word is correctly spelled? \nA. Accomodation B. Acommodation C. Accommodation D. Accommmodation"

print(Q7)
answer = input("answer: ").strip()
if answer.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q8 = "8. Choose the correct preposition: “She is good _____ Mathematics.” \nA. in B. on C. at D. with"
print(Q8)
answer = input("answer: ").strip()
if answer.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q9 = "9. What is the meaning of “procrastinate”? \nA. To work quickly B. To postpone something C. To complete something D. To explain something"
print(Q9)
answer = input("answer: ").strip()
if answer.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

Q10 = "10. Choose the correct sentence. \nA. Neither John nor James are present. B. Neither John nor James is present. C. Neither John or James is present. D. Neither John and James are present."
print(Q10)
answer = input("answer: ").strip()
if answer.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Wrong!")


print(f"Your total score is: {score}/10")

