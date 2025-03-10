# def fn1():
#     print("hello")
# fn1()
# def sum (a=9,b=5):
#     c=a+b
#     print(c)
# sum()   
# def sum (a=9,b=5):
#     return a+b
# print(sum(6,9)) 

# def today(date):
#     print("Today is", date)
# p = input("Enter today's date: ")
# today(p)

# recursion
# def factorial(i):
#     if i==0 or i==1:
#         return 1
#     else:
#         return i*factorial(i-1)
# print(factorial(int(input("Enter a no: "))))

# celesius to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius_temp = float(input("Enter temperature in Celsius: "))
# fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
# print("Temperature in Fahrenheit:", fahrenheit_temp)

# Rock, Paper, Scissors game
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()