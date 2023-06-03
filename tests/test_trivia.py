import pytest

from utils import gpt3_api
from game_logic.animal_generator import Animal, generate_animal
from game_logic.location import Location
from config import LOCATIONS, QUESTION_TYPES, TOTAL_MINI_GAMES, QUESTIONS_PER_GAME

def test_animal_generate_animal():
    animal = generate_animal('forest')
    assert animal is not None

def test_animal_generate_questions():
    animal = generate_animal('forest')
    assert len(animal.questions) == QUESTIONS_PER_GAME
    for question in animal.questions:
        assert question.question_text is not None
        assert question.correct_option is not None
        assert len(question.options) == 4

def test_animal_ask_question():
    animal = generate_animal('forest')
    question, correct_option, options = animal.ask_question()
    assert question is not None
    assert correct_option is not None
    assert len(options) == 4

def test_animal_get_summary():
    animal = generate_animal('forest')
    summary = animal.get_summary()
    assert summary is not None