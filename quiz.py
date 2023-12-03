print("Print Welcome to a Quiz.....")
name=input("Enter your name please...\n")
answer=input("Ready to play a Quiz (yes/no)")
score=0
total_question=3

if answer.lower()=='yes':
    answer=input("What country has the highest life expectancy?\n")

    if answer.lower()=='hong kong':
        score+=1
        print("Correct answer")

    else:
        print('Wrong')

    
    answer=input("Which is the capital of Australia?\n")
    if answer.lower()=='canberra':
        score+=1
        print("Correct Answer")
    
    else:
        print('Wrong')

    answer=input("Which is the largest coffee-producing state of India?\n")
    if answer.lower()=='karnataka':
        print("Correct")

    else:
        print("Wrong")


print(f"Thank you {name} for playing game with us your score is {score}")
marks=(score/total_question)*100
print("Marks optained is", marks)
print("Bye....")

