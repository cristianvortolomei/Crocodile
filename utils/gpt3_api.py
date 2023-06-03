import openai
from config import API_KEY

openai.api_key = API_KEY

def generate_text(prompt: str, max_tokens: int = 100, n: int = 1, stop: str = None, temperature: float = 0.5):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=stop,
        temperature=temperature
    )

    return response.choices[0].text.strip()