import random
playing = True
number = str(random.randint(1,10))
print("I will generate a number from 1 - 10 and you will have to guess the number....")
print("The game ends when you get 2 hero....")
while playing:
    guess = input("Give me your best guess >:D \n")
    if number == guess:
        print("You win the game.")
        print("The number was",number)
        break
    else:
        print("my point >:) you loose >:D \n")