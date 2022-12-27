# import question data and art and randint
from game_data import data
from art import logo, vs
import random
from replit import clear
# initialise variables
question_a = {}
question_b = {}
score = 0
user_guess = ''
message = ''
play_game = True


# create random questions
def get_random_question():
    """get random"""
    return random.choice(data)

    
#check question aren't the same
def check_questions_not_same(question_a, question_b):
    if question_a['name'] == question_b['name']:
        return True
    else:
        return False


# check if player is correct
def check_user_guess(user_guess, question_a, question_b):
    person_with_highest_follower_count = find_highest_followers(question_a, question_b)
    if user_guess.upper() == person_with_highest_follower_count:
        return True
    else:
        return False
    

def find_highest_followers(question_a, question_b):
    if question_a['follower_count'] > question_b['follower_count']:
        return 'A'
    else:
        return 'B'

        
#start the game
question_a = get_random_question()
# create loop for the game to choose next question b when player wins
while play_game:
    question_b = get_random_question()
    check_questions = check_questions_not_same(question_a, question_b)
    while check_questions:
        question_b = get_random_question()
        check_questions = check_questions_not_same(question_a, question_b)
    clear()
    print(logo)
    print(message)
    print(f"Compare A: {question_a['name']} a {question_a['description']} from {question_a['country']}: \n")
    print(vs)
    print(f"Against B: {question_b['name']} a {question_b['description']} from {question_b['country']}: \n ")
    #get player guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    #check if user guess is correct
    check_guess_correct = check_user_guess(user_guess, question_a, question_b)
    if check_guess_correct:
        score += 1
        message = f"You're right! Current score: {score}."
        question_a = question_b
    else:
        clear()
        print(logo)
        print(f"sorry, that's wrong. Final score: {score}")
        play_game = False