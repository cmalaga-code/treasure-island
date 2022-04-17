import draw
import logic

if __name__ == "__main__":
    draw.treasure()
    print("Welcome to treasure island!!")
    player_status = logic.first_trial()
    if player_status:
        print("Great Job! Next question..")
        player_status = logic.second_trial()
        if player_status:
            print("Great Job! You made the correct choice..")
            player_status = logic.thrid_trial()
            if player_status:
                print("You win !! Congrats !")
            else:
                print("Game Over!! Try again.")
        else:
            print("Game Over!! Try again.")
    else:
        print("Game Over!! Try again.")