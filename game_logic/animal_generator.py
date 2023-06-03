import random
import functools
from difflib import SequenceMatcher
from .question import Question
from utils.gpt3_api import generate_text
from config import QUESTION_TYPES, QUESTIONS_PER_GAME, LOCATIONS

def string_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

class Animal:
    def __init__(self, name: str, species: str, habitat: str, fact: str):
        self.name = name
        self.species = species
        self.habitat = habitat
        self.fact = fact
        self.facts = []
        self.questions = self.generate_questions()

    def generate_questions(self):
        questions = []
        for question_type in QUESTION_TYPES:
            prompt = f"What is the {question_type} of the {self.species}? (answer in a complex sentence, for example: 'It is a carnivore that eats insects and small animals', but in a way that a 5 year old could understand). Make sure you use 'it' as the subject of the sentence."
            correct_answer = generate_text(prompt)
            correct_answer = f"{correct_answer} (CORRECT ANSWER)"
            self.facts.append(correct_answer)
            wrong_answers = []
            for i in range(3):
                prompt = f"Make up something creative about the {question_type} of the {self.species} that is not true and fictional (answer in a complex sentence, for example: 'It is a carnivore that eats insects and small animals', but in a way that a 5 year old could understand). Make sure you use 'it' as the subject of the sentence."
                wrong_answer = generate_text(prompt, temperature=0.8)
                wrong_answers.append(wrong_answer)
            answer_options = [correct_answer] + wrong_answers
            random.shuffle(answer_options)
            question_text = f"What is the {question_type} of the {self.species}?"
            correct_option = answer_options.index(correct_answer) + 1
            questions.append(Question(question_text, correct_option, answer_options))
        return questions


    def ask_question(self):
        question = random.choice(self.questions)
        self.questions.remove(question)
        return question.question_text, question.correct_option, question.options

    def get_summary(self):
        prompt = f"Using the following facts about the {self.species}, write a summary of the animal in a way that a 5 year old could understand. Don't add any new facts, just use the ones below."
        for fact in self.facts:
            prompt += f"\n- {fact}"
        summary = generate_text(prompt, max_tokens=100, temperature=0.8)
        return summary

def generate_animal(location: str):

    prompt = f"Generate a fact about an animal found in {location}."
    fact = generate_text(prompt, max_tokens=30, temperature=0.8)

    prompt = f"Given this fact about an animal: {fact}. What species is the animal? (just the name of the species, for example: 'dog')"
    species = generate_text(prompt, max_tokens=30, temperature=0.2)

    name = functools.reduce(lambda x, y: x + " " + y.capitalize(), species.split(" ")).strip()

    return Animal(name, species, location, fact)
    