import pytest

'''Test - Pasamos la fixture'''
@pytest.mark.pruebaFixture
def test_sql(fxt_db, fxt_cursor, fake_persona):
    # region -- Creando a la persona --
    fxt_cursor.execute("INSERT INTO persona (nombre, apellido, id) VALUES (?, ?, ?)", fake_persona)
    #fxt_db.commit()
    # endregion

    # region -- Assert --
    persona = fxt_cursor.execute("SELECT * FROM persona WHERE persona.id=1").fetchone()
    print(persona)
    assert persona is not None
    #fxt_db.commit()
    # endregion
    # Tambien se puede hacer el clan up en cada función de prueba


