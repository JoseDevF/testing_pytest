


# Un mock es un objeto dummy, un objeto falso que devuelve
# lo que nosotros queremos o necesitamos para usar dentro del test.

from pruebas.monkey import MonkeyPatchOriginal


def test_greeting(monkeypatch):

    def mock_greeting():
        return "Hello, Test!"

    monkeypatch.setattr(MonkeyPatchOriginal, 'greeting', mock_greeting)

    print("\n\nAqui!!!", MonkeyPatchOriginal.greeting())

    assert MonkeyPatchOriginal.greeting() == "Hello, Test!"


class DatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url

    def connect(self):
        #Lógica para conectar a la base de datos
        pass

def test_database_connection(monkeypatch):
    db=DatabaseConnection('prod_db_url')


    monkeypatch.setattr((db, 'db_url', 'test_db_url'))

    assert db.db_url== 'test_db_url'



def get_config():
    return os.getenv('CONFIG', 'default')

def test_get_config(monkeypatch):

    monkeypatch.setenv('CONFIG', 'test_config')

    result = get_config()

    assert result == 'test_config'