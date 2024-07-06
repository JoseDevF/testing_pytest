import sqlite3
import pytest
import os

dbPath=os.path.abspath("../../test.db")

#Esta fixture prepara la base de datos del ambiente de pruebas y la limpia al finalizar las pruebas
@pytest.fixture()
def base_datos():
    print("\n\nArrange / Setup / Preconfiguración")
    # Conectar a la base de datos
    #db = sqlite3.connect("../test.db")
    db = sqlite3.connect(dbPath)
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
#Separar responsabilidades

@pytest.fixture()
def fxt_db():
    #db = sqlite3.connect(dbPath)
    db = sqlite3.connect("../test.db")
    print("\n\nConnection:", db)
    yield db
    db.close()

@pytest.fixture()
def fxt_cursor(fxt_db):
    cursor = fxt_db.cursor()
    print("\n\nConnection cursor:", cursor.connection)
    cursor.execute("DELETE FROM persona")
    yield cursor
    cursor.close()

@pytest.fixture()
def fake_persona():
    return ("Jose", "Hernández", 1)

