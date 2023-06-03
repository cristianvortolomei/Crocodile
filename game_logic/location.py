class Location:
    def __init__(self, name: str, habitat: str):
        self.name = name
        self.habitat = habitat

    def __str__(self):
        return f"{self.name} ({self.habitat})"