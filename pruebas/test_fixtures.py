import sqlite3
import pytest

#Esta fixture prepara la base de datos del ambiente de pruebas y la limpia al finalizar las pruebas
@pytest.fixture()
def base_datos():
    print("\n\nArrange / Setup / Preconfiguración")
    # Conectar a la base de datos
    db = sqlite3.connect("./test.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM persona")
    #db.commit()

    yield {"db":db, "cursor":cursor}

    print("\n\nCleanup / tear down / Limpíeza")
    # Limpiar base de datos
    cursor.execute("DELETE FROM persona")
    #db.commit()
    cursor.close()
    db.close()

#Esta fixture prepara la base de datos de producción


'''Test - Pasamos la fixture'''
@pytest.mark.pruebaFixture
def test_sql(base_datos):
    db = base_datos["db"]
    cursor = base_datos["cursor"]
    # region -- Creando a la persona --
    cursor.execute("INSERT INTO persona (nombre, apellido, id) VALUES (?, ?, ?)", ("Jose", "Hernández", 1))
    #db.commit()
    # endregion

    # region -- Assert --
    persona = cursor.execute("SELECT * FROM persona WHERE persona.id=1").fetchone()
    print(persona)
    assert persona is not None
    #db.commit()
    # endregion
    # Tambien mse puede hacer el clan up en cada función de prueba


