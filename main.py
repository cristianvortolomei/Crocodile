import sys
from game_logic.game import Game

def main():
    print("Welcome to Crocodile Explorer!")
    print("You are a curious crocodile exploring different habitats and learning about various animals.")
    
    game = Game()
    game.start()

    game.db_handler.close_connection()
    print("Thanks for playing Crocodile Explorer! See you next time.")

if __name__ == "__main__":
    main()