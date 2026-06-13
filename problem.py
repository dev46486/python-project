# we are going to write a program that generates a random number and ask the user to guess it. 
# if the players guess is higher then the actual number then the program displays "lower number please" similarly if the user guess is low then the program displays "higher number please" when the user guess the correct number the program displays the "the user guesses the correct number" 
import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a!=n):
    guesses += 1
    a = int(input("guess the number: "))
    if(a>n):
        print("lower number please")
    else:
        print("higher number please")
print(f"you have guessed the number {n} correctly in {guesses} attempts")