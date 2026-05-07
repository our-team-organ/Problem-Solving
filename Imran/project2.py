questions = ("Who is the real Madarchod?", "Who is the real Nigga?", "Who is the real Jhandu?", "Who is the real Bokachoda?", "Who is the Single?", "Who is the Bou-Pagol?", "Who is the Biyatta?", "Who is the Matal?")

options = (("A. Imran", "B. Durjoy", "C. Nahid", "D. Niloy"), ("A. Imran", "B. Durjoy", "C. Nahid", "D. Niloy"), ("A. Imran", "B. Durjoy", "C. Khalid", "D. Niloy"), ("A. Jubayer", "B. Durjoy", "C. Nahid", "D. Niloy"), ("A. Jubaraj", "B. Durjoy", "C. Nahid", "D. Niloy"), ("A. Imran", "B. Sayem", "C. Nahid", "D. Niloy"), ("A. Imran", "B. Durjoy", "C. Nahid", "D. Niloy"), ("A. Imran", "B. Durjoy", "C. Nahid", "D. Jubayer"))

answers = ("B", "D", "C", "A", "A", "B", "A", "C")

guesses = []

point = 0

q_num = 0

for question in questions:
    print(question)
    
    for option in options[q_num]:
        print(option)
    
    guess = input("Choose a Option (A/B/C/D): ").upper()

    guesses.append(guess)
    
    if(guess==answers[q_num]):
        print("Correct")
        point += 1
    else:
        print("Wrong Answer!")
        print(f"Correct Answer is {answers[q_num]}")

    q_num += 1
    
    
print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()
    
print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()
    
score = int(point / (len(questions)) * 100)
print(f"Your are {score}% right")