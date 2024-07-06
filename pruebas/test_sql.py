import sqlite3
import unittest


class TestSQL(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect("../test.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("DELETE FROM persona")
        self.db.commit()

    def test_crear_persona(self):
        # region -- Creando a la persona --
        self.cursor.execute("INSERT INTO persona (nombre, apellido, id) VALUES (?, ?, ?)", ("José", "Hernández", 1))
        self.db.commit()
        # endregion

        # region -- Assert --
        persona = self.cursor.execute("SELECT * FROM persona WHERE persona.id=1").fetchone()
        print(persona)
        assert persona is not None
        self.db.commit()
        # endregion
        # Tambien mse puede hacer el clan up en cada función de prueba

    def tearDown(self):
        # Limpiar base de datos
        self.cursor.execute("DELETE FROM persona")
        self.db.commit()
        self.cursor.close()
        self.db.close()