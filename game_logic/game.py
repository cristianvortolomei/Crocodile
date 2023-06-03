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
        for i in range(TOTAL_MINI_GAMES):
            location = self.select_location()
            animal = generate_animal(location)
            print(f"\nYou are in the {location} and meet a {animal.name}.")

            question_count = 0
            correct_answers = 0
            while question_count < QUESTIONS_PER_GAME:
                question, correct_option, options = animal.ask_question()
                print(f"\n{animal.name} asks: {question}")
                for index, option in enumerate(options, start=1):
                    print(f"{index}: {option}")

                answer = int(input("\nEnter your answer (1-4): "))
                if answer == correct_option:
                    print("Correct!")
                    correct_answers += 1
                    i += 1
                    print(f"DEBUG: correct_answers = {correct_answers}")
                    print(f"DEBUG: i = {i}")
                else:
                    i += 1
                    print(f"Oops! The correct answer was {options[correct_option - 1]}")
                    print(f"DEBUG: correct_answers = {correct_answers}")
                    print(f"DEBUG: i = {i}")

                question_count += 1

            if correct_answers == QUESTIONS_PER_GAME:
                print(f"Congratulations! You successfully completed the challenge with {animal.name}.")
                self.add_animal_to_notebook(location, animal)
            else:
                print(f"Better luck next time! {animal.name} encourages you to visit again.")

            self.show_notebook()

    def select_location(self):
        location = random.choice(LOCATIONS)
        while location in self.visited_locations:
            location = random.choice(LOCATIONS)
        self.visited_locations.append(location)
        return location

    def add_animal_to_notebook(self, location, animal):
        animal_summary = animal.get_summary()
        self.notebook[location] = animal_summary
        self.db_handler.add_animal((animal.name, animal.species, animal.habitat, animal_summary))

    def show_notebook(self):
        print("\n\nYour notebook has the following information:")
        for location, animal_summary in self.notebook.items():
            print(f"\nLocation: {location}")
            print(animal_summary)