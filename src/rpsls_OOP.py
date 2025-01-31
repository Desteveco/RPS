import random
from src.game_action import GameAction
from src.game_result import GameResult
from src.victories import VICTORIES

class Game:
    def __init__(self):
        self.rounds_won_player = 0
        self.rounds_won_computer = 0
        pass
        

    def assess_game(self, user_action, computer_action):

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
            return GameResult.Tie

        if  computer_action in VICTORIES[user_action]:
            print("You Loose!")
            self.rounds_won_computer += 1
            return GameResult.Defeat

        else:
            print("You Win!")
            self.rounds_won_player += 1
            return GameResult.Victory


    def get_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")
        return computer_action


    def get_user_action(self):
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)
        return user_action


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


    def main(self):

        while True:
            try:
                user_action = self.get_user_action()
            except ValueError:
                range_str = f"[0, {len(GameAction) - 1}]"
                print(f"Invalid selection. Pick a choice in range {range_str}!")
                continue

            computer_action = self.get_computer_action()
            self.assess_game(user_action, computer_action)
            print(f"Player: {self.rounds_won_player} | Computer: {self.rounds_won_computer}")
            
            if self.rounds_won_player == 3 or self.rounds_won_computer == 3:
                print(f"{'Player' if self.rounds_won_player == 3 else 'Computer'} wins the game!")
                break 
                
        self.play_another_round()


if __name__ == "__main__":
    
    game = Game()
    game.main()