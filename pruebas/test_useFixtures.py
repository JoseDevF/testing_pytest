# test_database.py
import pytest

# Aplica las fixtures a toda la clase
@pytest.mark.usefixtures("db_connection", "setup_database")
class TestDatabase:

    def test_persona_table_exists(self, db_connection):
        print("Running test_persona_table_exists")
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='persona_alternative';")
        result = cursor.fetchone()
        assert result is not None, "La tabla 'persona_alternative' no existe."
        print("Resultados de la consulta:", result)

    def test_inserted_data(self, db_connection):
        print("Running test_inserted_data")
        cursor = db_connection.cursor()
        cursor.execute("SELECT nombre, edad FROM persona_alternative WHERE nombre = ?", ("Alice",))
        result = cursor.fetchone()
        assert result == ("Alice", 30), "Los datos de Alice no se encontraron correctamente."
        print("Datos de Alice recuperados:", result)

    def test_multiple_rows(self, db_connection):
        print("Running test_multiple_rows")
        cursor = db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM persona_alternative")
        result = cursor.fetchone()
        assert result[0] == 2, "El número de filas en la tabla 'persona_alternative' no es el esperado."
        print("Número de filas en persona_alternative:", result[0])
