import random

class Game:
    game_items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        while True:
            user_item = input("Select rock(r), paper(p) or scissors (s): ").lower()
            letter_of_items = [i[0] for i in self.game_items]
            if user_item == 'p':
                user_item = 'paper'
            elif user_item == 'r':
                user_item = 'rock'
            elif user_item == 's':
                user_item = 'scissors'
            if user_item in self.game_items:
                return user_item
            else:
                print("Invalid input please try again. Your choice must be: rock(r), paper(p), or scissors(s)")

    def get_computer_item(self):
        computer_item = random.choice(self.game_items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        # user_item = self.get_user_item()
        # computer_item = self.get_computer_item()
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == 'scissors') or (user_item == "paper" and computer_item == 'rock') or (user_item == 'scissors' and computer_item == 'paper'):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
        if game_result == "draw":
            print(f"You selected {user_item}. The computer selected {computer_item}. You drew!")
            return game_result
        elif game_result == "loss":
            print(f"You selected {user_item}. The computer selected {computer_item}. You lose!")
            return game_result
        else:
            print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
            return game_result


# game1 = Game()
# game1.play()