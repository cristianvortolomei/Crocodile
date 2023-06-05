import random
from .location import Location
from .animal_generator import generate_animal
from config import LOCATIONS, QUESTIONS_PER_GAME, TOTAL_MINI_GAMES
from database.database_handler import DatabaseHandler

class Game:
    def __init__(self):
        self.notebook = {}
        self.visited_locations = []
        self.db_handler = DatabaseHandler()

    def start(self):
        try:
            for i in range(TOTAL_MINI_GAMES):
                location = self.select_location()
                animal = generate_animal(location)
                if animal is None:
                    print("Error generating animal. Skipping to next game.")
                    continue
                print(f"\nYou are in the {location} and meet a {animal.name}.")

                question_count = 0
                correct_answers = 0
                while question_count < QUESTIONS_PER_GAME:
                    question, correct_option, options = animal.ask_question()
                    print(f"\n{animal.name} asks: {question}")
                    for index, option in enumerate(options, start=1):
                        print(f"{index}: {option}")

                    while True:
                        try:
                            answer = int(input("\nEnter your answer (1-4): "))
                            if answer < 1 or answer > 4:
                                print("Invalid input. Please enter a number between 1 and 4.")
                                continue
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 and 4.")
                            continue

                    if answer == correct_option:
                        print("\nCorrect!\n")
                        correct_answers += 1
                        i += 1
                    else:
                        i += 1
                        print(f"Oops! The correct answer was {options[correct_option - 1]}")

                    question_count += 1

                if correct_answers == QUESTIONS_PER_GAME:
                    print(f"\n\nCongratulations! You successfully completed the challenge with: {animal.name}.\n{animal.name} is now in your notebook.\n\n")
                    self.add_animal_to_notebook(location, animal)
                else:
                    print(f"\n\nBetter luck next time! {animal.name} encourages you to visit again.\n\n")

            print("\n\nGame over! Here is your notebook:")
            self.show_notebook()
            print("\n\nThank you for playing Crocodile Explorer!\n\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    def select_location(self):
        try:
            location = random.choice(LOCATIONS)
            while location in self.visited_locations:
                location = random.choice(LOCATIONS)
            self.visited_locations.append(location)
            return location
        except Exception as e:
            print(f"Error selecting location: {e}")
            return None

    def add_animal_to_notebook(self, location, animal):
        try:
            animal_summary = animal.get_summary()
            self.notebook[location] = animal_summary
            self.db_handler.add_animal((animal.name, animal.species, animal.habitat, animal_summary))
        except Exception as e:
            print(f"Error adding animal to notebook: {e}")

    def show_notebook(self):
        try:
            for location, animal_summary in self.notebook.items():
                print(f"\nLocation: {location}")
                print(animal_summary)
        except Exception as e:
            print(f"Error showing notebook: {e}")