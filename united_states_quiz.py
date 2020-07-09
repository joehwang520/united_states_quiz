#Quiz v1.11
#Number of end user tests: 1
print("How well do you know about the United States? Test yourself to find out!")
print("The questions will get progressively harder. Try to answer all of them correctly! ")
print(f"\n--Please capitalize all of your answers unless instructed otherwise. Otherwise they will NOT count!--\n")

score = 0

#Question 1
question1 = "1. How many stars are there in the United States? (Only numbers will be accepted.) "
answer1 = input(question1)
answer1 = int(answer1)

if answer1 == 50:
    print(f"Correct!\n")
    score += 1
else:
    print(f"Sorry, that is incorrect.\n")


#Question 2
question2 = "2. How many stripes are there in the U.S. flag? (Only numbers will be accepted.) "
answer2 = input(question2)
answer2 = int(answer2)

if answer2 == 13:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 3
question3 = "3. Name one of the colors of the U.S. flag. (This does NOT have to be capitalized.) "
answer3 = input(question3)

if answer3 == "red" or answer3 == "Red" or answer3 == "blue" or answer3 == "Blue" or answer3 == "white" or answer3 == "White":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 4
question4 = "4. Who was the first president of the United States? "
answer4 = input(question4)

if answer4 == "George Washington" or answer4 == "Washington":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 5
question5 = "5. What continent is the United States in? "
answer5 = input(question5)

if answer5 == "North America":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 6
question6 = "6. Name any U.S. state that shares a border with Mexico: "
answer6 = input(question6)

if answer6 == "California" or answer6 == "Arizona" or answer6 == "New Mexico" or answer6 == "Texas":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 7
question7 = "7. Name any of the five Great Lakes: "
answer7 = input(question7)

if answer7 == "Erie" or answer7 == "Huron" or answer7 == "Michigan" or answer7 == "Ontario" or answer7 == "Superior":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 8
question8 = "8. Name any of the three branches of the U.S. government (Don't forget to capitalize): "
answer8 = input(question8)

if answer8 == "Legislative" or answer8 == "Executive" or answer8 == "Judicial":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 9
question9 = "9. Who is on the back of the $50 bill? "
answer9 = input(question9)

if answer9 == "Grant" or answer9 == "Ulysses Grant" or answer9 == "Ulysses S. Grant":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 10
question10 = "10. How many years does a president serve in a single term? (Only numbers will be accepted.) "
answer10 = input(question10)
answer10 = int(answer10)


if answer10 == 4:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 11
question11 = "11. Franklin Delano Roosevelt was the only president to serve more than 2 terms. How many terms did he serve? (Only numbers will be accepted.) "
answer11 = input(question11)
answer11 = int(answer11)


if answer11 == 4:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 12
question12 = "12. Which president served for only 31 days? "
answer12 = input(question12)


if answer12 == "Harrison" or answer12 == "William Harrison" or answer12 == "William Henry Harrison":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 13
question13 = "13. Which year was the 27th amendment ratified? (Only numbers will be accepted.) "
answer13 = input(question13)
answer13 = int(answer13)


if answer13 == 1992:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 14
question14 = "14. Which year was Hawaii admitted to the Union? (Only numbers will be accepted.) "
answer14 = input(question14)
answer14 = int(answer14)


if answer14 == 1959:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 15
question15 = "15. Which year did the American Civil War end? (Only numbers will be accepted.) "
answer15 = input(question15)
answer15 = int(answer15)


if answer15 == 1865:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")




percent = int((score/15)*100)

print(f"You answered {score} question(s) correctly! Your scored {percent}%!\n")
