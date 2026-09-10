import random
def get_choices():
    player_choice=input("Rock : Paper : Scissors ;Choose one")
    options=["Rock","Paper","Scissors"]
    Computer_choice=random.choice(options)
    choices={"player": player_choice ,"Computer":Computer_choice}
    return choices
def check_win(player,computer):
    print(f" you chose {player} and Computer chose {computer}")
    if player == computer:
        return "Its a Tie"
    elif player=="Rock":
        if computer=="Scissors":
            return "Rock smashes the Scissors! You Win"
        else:
            return "Paper wraps the Rock! You Lose"
    elif player=="Paper":
        if computer=="Rock":
            return "Paper wraps the Rock! You Win"
        else:
            return "Scissors cut  the Paper! You Lose"
    elif player=="Scissors":
        if computer=="Paper":
            return "Scissors cut  the Paper! You Win"
        else:
            return "Rock smashes the Scissors! You Lose"
Choices=get_choices()
result=check_win(Choices["player"],Choices["Computer"])
print(result)