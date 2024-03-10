from random import randint


print("Welcome to the Math Quiz Game!!")

playing = input("Do you want to start the quiz? (y/n) ")


while playing.lower() not in ('y', 'n', 'yes', 'no'):
    print("You should type 'y' or 'n' !!") 
    playing = input("Do you want to start the quiz? (y/n) ")
    
if playing.lower() not in ('y', 'yes'):
        quit()
else:
    print("let's start our quiz, ready :)")
    
score = 0

for i in range(5):
    x = randint(1, 999)
    y = randint(1, 999)
    answer = int(input( str(x) + " + " + str(y) + " =  "))
    
    if x + y == answer:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("Your score is:", str(score), "points")