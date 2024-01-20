import random

guess_count = 10


print('***************************')
print('***************************')
print('***************************')
print('**** WELCOME TO STARLITECODE GUESSSING GAME WITH PYTHON ****')
print('***************************')
print('***************************')
print('***************************')

while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStart Game__(1) \nGame Rules___(2)\nQuit_______(3) \n: ').lower()

    if response == '1':
        print('*****')
        print('*****')
        print('*****')
        name = input('Please Enter Your Name to Start\n:')
        while True:
            while guess_count != 0:
                secret_number = random.randint(1, 5)
                print('*** PLAYER ' + name.upper() + ' ***')
                print(secret_number)
                print('Your Score is ' + str(guess_count))
                print('*****')
                print('*****')
                try:
                    guess = int(input('Take Guess from 1-10: '))
                    if guess == secret_number:
                        print("***** Congratlations Your Guessed was right, you earn a point ")
                        guess_count += 1
                    elif guess > 5:
                        
                        break
                    else:
                        print("***** Sorry!! Your Guessed was wrong, a point is deducted from your points ")
                        guess_count -= 1
                        print('Your Score is ' + str(guess_count))
                except:
                    print("** CHOOSE FROM 1-5 *** ")
                    print('*****')
            print("***** GAME OVER *** ")
            print('*****')
            print('*****')
            break
    elif response == '2':
        print('***************************')
        print('***************************')
        print('**** GAME RULES ****')
        print('1. The system Generates a random number from 1-5 ')
        print('2. You have unlimited trials ')
        print('3. If your guessing is right you won and you will get a score increases ')
        print("4. Game over if only your score is 0 ")
        print("5. To Quit Game enter a number greater than 5")
        print('*****')
        print('*****')
        print('*****')
    elif response == '3':
        quit()
    else:
        print('*****')
        print('*****')
        print('SELECT A VALID NUMBER FROM 1-3 TO CONTINUE')
        print('*****')
        print('*****')
	
