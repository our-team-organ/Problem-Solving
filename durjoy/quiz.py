questions = (("how many days in a week? "),
             ("capital of bangladesh? "),
             ("how many bones in human body? "),
             ("what is the colour of the sky? "))
options   = (("A.7","B.8","C.9","D.5"),
             ("A.comilla","B.brahmanbaria","C.dhaka","D.japan"),
             ("A.205","B.206","C.207","D.208"),
             ("A.blue","B.red","C.yellow","D.white"))

answers = ("A","C","B","A")
guesses=[]
scrore=0
question_num=0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter the answer: ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT!")
        scrore +=1
    else:
        print("INCORRECT MOTHERFUCKER")

    question_num +=1


print("~~~~~~~~~~RESULT~~~~~~~~~~~")
print("ANSWERS: ",end=" ")
for answer in answers:
 print(answer,end=" ")
print()

print("GUESSES: ",end=" ")
for guess in guesses:
   print(guess,end=" ")
print()

scrore = int(scrore/len(questions) * 100)

print(f"your scrore is {scrore}%")