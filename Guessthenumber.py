import random
number = random.randint(1,100)
print("welcome to guess the number game! \n Guess a number between 1 to 100")
flag = 1
while flag==1:
    j=0
    for attempts in range (1,7):
        n = int(input("Take A Guess:"))
        if n >number:
            print ("number is too high!")
        elif n < number:
                print("The Number Is Too Low!")
        else:
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            j = 1
            break
    if j==0:
        print("Out of attempts!\n Try your luck next time.")
        print("\n")
        print("Do you want to continue the game?")
        print("Enter 1 to continue and 0 to exit")
        flag = int (input("Enter your choice:"))           
           


