import requests
import pytest
import sqlite3
import os


# Fixture parametrizada para diferentes archivos de base de datos SQLite
@pytest.fixture(params=[
    "test_db_1.sqlite",
    "test_db_2.sqlite",
    "test_db_3.sqlite"
])
def sqlite_db(request):
    # Crear la base de datos temporalmente para la prueba
    db_name = request.param
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Crear una tabla de ejemplo
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    conn.commit()

    # Proporcionar la conexión a la prueba
    yield conn

    # Cerrar la conexión y eliminar el archivo de la base de datos al final de la prueba
    conn.close()
    os.remove(db_name)


def test_sqlite_connection(sqlite_db):
    cursor = sqlite_db.cursor()

    # Verificar que podemos conectarnos y realizar una consulta
    cursor.execute("SELECT name FROM users")
    rows = cursor.fetchall()

    assert len(rows) == 2
    assert rows[0][0] == 'Alice'
    assert rows[1][0] == 'Bob'


# Fixture parametrizada para diferentes endpoints de la API
@pytest.fixture(params=[
    "https://dummyapi.online/api/users",
    "https://dummyapi.online/api/pokemon",
    "https://dummyapi.online/api/products"
])
def fake_api_endpoint(request):
    return request.param

def test_api_response(api_endpoint):

    response = requests.get(api_endpoint)
    print(f"\n\n{api_endpoint}\n\n")
    print(f"\n\n{response.content}\n\n")

    assert response.status_code == 200
