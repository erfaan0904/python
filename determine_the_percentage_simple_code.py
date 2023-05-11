rq = int(input("Enter the correct number of selected questions..: "))  # right questions number
wq = int(input("Enter the number of wrongly selected questions..: "))  # wrong questions number
tq = int(input("Enter total number of course questions..........: "))  # Total number of course questions
lp = (((rq * 3) - wq) / (tq * 3)) * 100
print("Your lesson percentage : ", lp)