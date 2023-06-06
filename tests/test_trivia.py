import pytest
from game_logic.animal_generator import Animal, generate_animal
from config import QUESTIONS_PER_GAME

def test_animal_init():
    animal = Animal("Lion", "Panthera leo", "Savannah", "Lions are the only cats that have manes.")
    assert animal.name == "Lion"
    assert animal.species == "Panthera leo"
    assert animal.habitat == "Savannah"
    assert animal.fact == "Lions are the only cats that have manes."
    assert len(animal.questions) == QUESTIONS_PER_GAME

def test_animal_generate_questions():
    animal = generate_animal("forest")
    assert len(animal.questions) == QUESTIONS_PER_GAME
    for question in animal.questions:
        assert question.question_text is not None
        assert question.correct_option is not None
        assert len(question.options) == 4

def test_animal_ask_question():
    animal = generate_animal("forest")
    question, correct_option, options = animal.ask_question()
    assert question is not None
    assert correct_option is not None
    assert len(options) == 4

def test_animal_get_summary():
    animal = generate_animal("forest")
    summary = animal.get_summary()
    assert summary is not None
    
def test_generate_animal():
    animal = generate_animal("forest")
    assert animal is not None
    assert animal.habitat == "forest"
    assert animal.fact is not None
    assert animal.species is not None
    assert animal.name is not None

def test_animal_generate_animal_questions():
    animal = generate_animal("forest")
    assert len(animal.questions) == QUESTIONS_PER_GAME

def test_animal_generate_animal_questions_type():
    animal = generate_animal("forest")
    for question in animal.questions:
        assert question.question_text.startswith("What is the")
        assert question.question_text.endswith(f"of the {animal.species}?")
        assert question.correct_option in [1, 2, 3, 4]
        assert len(question.options) == 4

def test_animal_generate_animal_questions_options():
    animal = generate_animal("forest")
    for question in animal.questions:
        assert question.correct_option in [1, 2, 3, 4]
        assert len(question.options) == 4
        assert question.correct_option <= len(question.options)
        assert question.options[question.correct_option - 1].endswith("(CORRECT ANSWER)")

def test_animal_ask_question_remove():
    animal = generate_animal("forest")
    question, correct_option, options = animal.ask_question()
    assert question is not None
    assert correct_option is not None
    assert len(options) == 4
    assert question not in animal.questions

def test_animal_generate_questions_type():
    animal = generate_animal("forest")
    for question in animal.questions:
        assert question.question_text.startswith("What is the")
        assert question.question_text.endswith(f"of the {animal.species}?")
        assert question.correct_option in [1, 2, 3, 4]
        assert len(question.options) == 4

def test_animal_generate_questions_options():
    animal = generate_animal("forest")
    for question in animal.questions:
        assert question.correct_option in [1, 2, 3, 4]
        assert len(question.options) == 4
        assert question.correct_option <= len(question.options)
        assert question.options[question.correct_option - 1].endswith("(CORRECT ANSWER)")

def test_animal_generate_questions_facts_options():
    animal = generate_animal("forest")
    for fact in animal.facts:
        assert fact.endswith("(CORRECT ANSWER)")
        assert fact in [question.options[question.correct_option - 1] for question in animal.questions]

def test_animal_generate_questions_facts_remove():
    animal = generate_animal("forest")
    for fact in animal.facts:
        assert fact.endswith("(CORRECT ANSWER)")
        assert fact in [question.options[question.correct_option - 1] for question in animal.questions]
    animal.questions = []
    animal.facts = []
    assert len(animal.questions) == 0
    assert len(animal.facts) == 0