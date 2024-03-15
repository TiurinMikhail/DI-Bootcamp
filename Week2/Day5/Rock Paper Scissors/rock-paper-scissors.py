from game import Game

def get_user_menu_choice():
    print('     MENU\n', '(g) Play a new game\n', '(x) Show scores\n', '(q) Quit\n')
    valid_input = ['g', 'x', 'q']
    while True:
        user_input = input('Enter your choice: ').lower()
        if user_input in valid_input:
            return user_input
        else:
            print("Invalid choice. Please enter 'g', 'x', or 'q'.")


def print_results(results):
    for key, value in results.items():
        print(f'{key} : {value}')


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        user_input = get_user_menu_choice()
        if user_input == 'g':
            user_game = Game()
            result = user_game.play()
            results[result] += 1

        elif user_input == 'x':
            print_results(results)

        elif user_input == 'q':
            print('Game Results:\n')
            print(f'You won {results["win"]} times')
            print(f'You lost {results["loss"]} times')
            print(f'You drew {results["draw"]} times')
            break

# Try
main()
