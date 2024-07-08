import os
import sqlite3
import pytest


@pytest.fixture(scope='class')
def db_connection():
    # Obtén la ruta absoluta del archivo de la base de datos
    db_path = os.path.abspath("test.db")
    # print(f"Conectando a la base de datos en: {db_path}")

    # Establece la conexión a la base de datos
    conn = sqlite3.connect(db_path)
    yield conn
    conn.close()


@pytest.fixture(scope='class', autouse=True)
def setup_database(db_connection):
    cursor = db_connection.cursor()
    # Configura la tabla de prueba
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persona_alternative (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            edad INTEGER
        )
    ''')
    cursor.execute('''
        DELETE FROM persona_alternative;
    ''')
    db_connection.commit()

    # Inserta datos de prueba
    cursor.execute('INSERT INTO persona_alternative (nombre, edad) VALUES (?, ?)', ("Alice", 30))
    cursor.execute('INSERT INTO persona_alternative (nombre, edad) VALUES (?, ?)', ("Bob", 25))
    db_connection.commit()
