print("welcome to my quiz game")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
     quit()

print("okay, lets plays :)")
score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("do animals have sex? ")
if answer.lower() == "yes":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("who's the president of Nigeria ")
if answer.lower() == "buhari":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what year did Bob Marley died? ")
if answer.lower() == "1977":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What's the tallest mountain in the world? ")
if answer.lower() == "Mt Everest":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what sickness is associated with tse-tse fly? ")
if answer.lower() == "sleeping sickness":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("what is the meaning of SCAM? ")
if answer.lower() == "still chasing after money":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("who's the first president of Nigeria ")
if answer.lower() == "Tafawa Balewa":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 8) * 100) + "%.")
