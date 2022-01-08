from  high_lower import game_data
import random

def format(account):
    """This will format your data in a line."""
    account_name=account["owner"]
    account_prof=account["profession"]
    account_country=account["country"]
    return(f"{account_name} , {account_prof} from {account_country}")


def followers_checker():
    account_a_follower =account_a["followers"]
    account_b_follower =account_b["followers"]
    if account_a_follower >account_b_follower:
        return "a"
    else:
        return "b"
start = True
score = 0
restart_game = True

while restart_game:
    while start:

        account_a = random.choice(game_data)
        account_b = random.choice(game_data)
        # print(account_b)

        # print(account_a)
        if account_a == account_b:
            account_b = random.choice(game_data)
        print(f"Compare account A : {format(account_a)}")
        print(f"Against account B: {format(account_b)}")

        guess = input("Guess which has more follower 'A' or 'B' : ").lower()

        if guess == followers_checker():
            score += 1
            print("You Win")
        else:
            start = False
            print("You Lose")
            print(f"Your score : {score}\n")


    restart_game = input("Type 'True' to restart the game : ").lower()
    if restart_game == "true":
        start = True



