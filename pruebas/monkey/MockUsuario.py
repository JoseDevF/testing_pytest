import requests
import pytest
from unittest.mock import MagicMock, patch

#from user import User


class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.uname = None
        self.email = None

    def fetch_user_data(self):
        url = f"https://dummyapi.online/api/users/{self.user_id}"
        response = requests.get(url)
        data = response.json()
        self.uname = data.get('username')
        self.email = data.get('email')


    def send_email(self, subject, message):
        print(f"Sending email to {self.email}: {subject} - {message}")




def test_user_magic_mock():
    # Creamos un MagicMock para simular un objeto User
    user_mock = MagicMock(spec=User)

    # Configuramos los atributos que queremos simular
    user_mock.user_id = 123  # Ejemplo de un user_id específico para la prueba
    user_mock.uname = "mock_username"
    user_mock.email = None # Simulamos que viene vacío el correo

    # Podemos simular métodos específicos si es necesario,
    # como fetch_user_data o send_email
    # Por ejemplo, para simular fetch_user_data:
    user_mock.fetch_user_data.return_value = None  # Simulamos que no hay retorno

    # Para simular send_email:
    user_mock.send_email.return_value = None  # Simplemente simulamos la ejecución del método

    # Ahora podemos usar user_mock en nuestras pruebas
    # Por ejemplo, podemos llamar a métodos y verificar su
    # comportamiento simulado
    user_mock.fetch_user_data()
    user_mock.send_email("Subject dummy", "Body message")

    # También podemos hacer aserciones sobre cómo se llamaron
    # los métodos, por ejemplo:
    user_mock.fetch_user_data.assert_called_once()  # Verifica que fetch_user_data haya sido llamado exactamente una vez
    user_mock.send_email.assert_called_once_with("Subject dummy", "Body message")  # Verifica cómo se llamó send_email



def test_fetch_user_data():
    user = User(1)

    # Faltaba mandar llamar al método para que consultara la API con
    # el id que creamos el objeto user
    user.fetch_user_data()

    print("\n\n",user.uname, user.email )

    assert True



