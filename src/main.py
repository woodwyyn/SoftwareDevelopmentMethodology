# src/main.py

from games.game_geom_prog import GeometricProgressionGame
from games.game_scm import SmallestCommonMultipleGame


def select_game(game_name):
    if game_name == "geom_prog":
        return GeometricProgressionGame()
    elif game_name == "smallest_common_multiple":
        return SmallestCommonMultipleGame()
    else:
        raise ValueError(f"Game '{game_name}' not found.")

def main():
    print("Available games:\n"
	"1. Geometric Progression\n"
	"2. Least Common Multiple\n")
    game_choice = input("Choose a game (1 or 2): ")

    try:
        if game_choice == "1":
            selected_game = select_game("geom_prog")
            selected_game.choose_difficulty()
        elif game_choice == "2":
            selected_game = select_game("smallest_common_multiple")
        else:
            raise ValueError("\nInvalid game choice.")
        
        selected_game.start()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()