import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='animals.db'):
        self.db_name = db_name
        self.conn = self.create_connection()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)

        if conn:
            self.conn = conn
            self.create_animals_table()

        return conn

    def create_animals_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,   
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            habitat TEXT NOT NULL,
            fact TEXT NOT NULL
        );
        """

        try:
            self.conn.execute(query)
        except sqlite3.Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def add_animal(self, animal_data):
        query = """
        INSERT INTO animals(name, species, habitat, fact)
        VALUES (?, ?, ?, ?);
        """

        cur = self.conn.cursor()
        cur.execute(query, animal_data)
        self.conn.commit()
        return cur.lastrowid

    def get_animal(self, animal_id):
        query = """
        SELECT * FROM animals WHERE id = ?;
        """

        cur = self.conn.cursor()
        cur.execute(query, (animal_id,))
        return cur.fetchone()

    def get_all_animals(self):
        query = """
        SELECT * FROM animals;
        """

        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()