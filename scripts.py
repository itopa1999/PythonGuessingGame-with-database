# Builtin imports
import random
import sqlite3
import getpass
import string



# Function to update high score in the database
def update_high_score(player_name, score):
    # Check if the player already exists in the database
    cursor.execute("SELECT * FROM high_scores WHERE player_name=?", (player_name,))
    existing_player = cursor.fetchone()

    if existing_player:
        # If the player exists, update the score if the new score is higher
        if score > existing_player[1]:
            cursor.execute("UPDATE high_scores SET score=? WHERE player_name=?", (score, player_name))
    else:
        # If the player doesn't exist, insert a new record
        cursor.execute("INSERT INTO high_scores (player_name, score) VALUES (?, ?)", (player_name, score))

    # Commit the changes to the database
    conn.commit()

# Function to authenticate user or create a new user
def authenticate_user():
    while True:
        player_name = input("Enter your name: ")
        password = str(getpass.getpass('Enter your password: '))

        cursor.execute("SELECT * FROM users WHERE player_name=? AND password=?", (player_name, password))
        existing_user = cursor.fetchone()
        
        if existing_user:
            # If the player name exists, check the password
            if password == existing_user[1]:
                print('***************************')
                print('***************************')
                print('***************************')
                print('***************************')
                print(f"Welcome back, {player_name}!")
                return player_name
            else:
                print("Incorrect password. Please try again.")
                break
        else:
            create_new_user(player_name, password)

# Function to create a new user
def create_new_user(player_name, password):
    cursor.execute("INSERT INTO users (player_name, password) VALUES (?, ?)", (player_name, password))
    conn.commit()
    print('***************************')
    print('***************************')
    print('***************************')
    print(f"Player {player_name} created successfully!")
    print('***************************')
    
    print("Enter Your name and password again")
    

# Function to reset user password
def reset_password(player_name):
    new_password = input("Enter your new password: ")
    cursor.execute("UPDATE users SET password=? WHERE player_name=?", (new_password, player_name))
    conn.commit()
    print("Password reset successful!")

# Function to list players and their high scores
def list_players_high_scores():
    cursor.execute("SELECT * FROM high_scores ORDER BY score DESC")
    high_scores = cursor.fetchall()

    if not high_scores:
        print("No high scores available.")
    else:
        print("***** HIGH SCORES *****")
        for player in high_scores:
            print(f"{player[0]}: {player[1]}")
        print('*****')

# Connect to the database
conn = sqlite3.connect('guessing_python.db')
cursor = conn.cursor()

# Create users and high_scores tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        player_name TEXT PRIMARY KEY,
        password TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS high_scores (
        player_name TEXT PRIMARY KEY,
        score INTEGER
    )
''')
conn.commit()

# Set default guess count
guess_count = 10

# Welcome screen
print('***************************')
print('***************************')
print('***************************')
print('**** WELCOME TO STARLITECODE GUESSING GAME WITH PYTHON ****')
print('***************************')
print('***************************')
print('***************************')

while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStart Game__(1) \nGame Rules___(2)\nHigh Scores__(3)\nReset Database__(4)\nQuit_______(5)\n: ').lower()

    if response == '1':
        print('*****')
        print('*****')
        print('*****')
        # Authenticate or create a new user
        player_name = authenticate_user()

        while True:
            # Start Game
            while guess_count != 0:
                secret_number = random.randint(1, 5)
                print('*** PLAYER ' + player_name.upper() + ' ***')
                print(secret_number)
                print('Your Score is ' + str(guess_count))
                print('*****')
                print('*****')
                try:
                    # Check if the guessing is right and add 1 score to the player scores
                    guess = int(input('Take Guess from 1-5: '))
                    if guess == secret_number:
                        print("***** Congratulations! Your Guessed was right, you earn a point ")
                        guess_count += 1
                        update_high_score(player_name, guess_count)
                    # if player enters a value greater than 5, the game quits
                    elif guess > 5:
                        break
                    # if guessing is wrong, deduct 1 from the player scores
                    else:
                        print("***** Sorry!! Your Guessed was wrong, a point is deducted from your points ")
                        guess_count -= 1
                        print('Your Score is ' + str(guess_count))
                except ValueError:
                    print("** CHOOSE FROM 1-5 *** ")
                    print('*****')
            print('*****')
            print('*****')
            print("***** GAME OVER *** ")
            print('*****')
            print('*****')
            break
            
    elif response == '2':
        # Display game rules
        print('***************************')
        print('***************************')
        print('**** GAME RULES ****')
        print('1. The system Generates a random number from 1-5 ')
        print('2. You have unlimited trials ')
        print('3. If your guessing is right, you win and your score increases ')
        print("4. Game over only if your score is 0 ")
        print("5. To Quit the game, control + Z")
        print('*****')
        print('*****')
        print('*****')
    elif response == '5':
        # Quit the game
        quit()
    elif response == '3':
        # List players and their high scores
        print('***************************')
        print('***************************')
        print('***************************')
        list_players_high_scores()
    elif response == '4':
        # Reset the entire database
        print('***************************')
        print('***************************')
        print('***************************')
        confirm_reset = input("Are you sure you want to reset the entire database? (yes/no): ").lower()
        if confirm_reset == 'yes':
            cursor.execute("DELETE FROM users")
            cursor.execute("DELETE FROM high_scores")
            conn.commit()
            print("Database reset successful!")
        else:
            print("Reset canceled.")
    else:
        # Invalid input
        print('*****')
        print('*****')
        print('SELECT A VALID NUMBER FROM 1-5 TO CONTINUE')
        print('*****')
        print('*****')
