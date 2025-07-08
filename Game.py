from Dice_Game_With_Computer import Dice
from Players import Player


class Game:
    def __init__(self, dice, player):
        self.dice= dice
        self.player=player

    def game_start(self):
        i=0
        print("Welcome to Game ")
        while self.dice.counter>0 and Player.counter>0:
            print(f"Round {i}")

            user_input = int(input("Enter the number between 0 to 6 :-"))
            dice_result= self.dice.roll_dice()
            print(f"User Dice result: {user_input}")
            print(f"Dice result :{dice_result}")

            if user_input>dice_result:
                self.player.counter-=1
                print("USER WIN POINT REDUCE ",self.player.counter)
            elif user_input<dice_result:
                self.dice.counter -=1
                print("SYSTEM WIN POINT REDUCE ", self.dice.counter)
            elif user_input==dice_result:
                print("DRAW")
            else:
                if self.player.counter==0:
                    print("Player win")
                else:
                    print("System Win")
            i += 1

            


dice = Dice()
player = Player(value=0)

# Start the game
game = Game(dice, player)
game.game_start()
