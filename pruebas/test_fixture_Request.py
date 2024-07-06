# test_fixture_request.py
import pytest

# Fixture que utiliza FixtureRequest para obtener información dinámica
@pytest.fixture
def ejemplo_fixture(request):
    print("\nEjecutando fixture ejemplo_fixture")
    # Accediendo a la función de prueba actual
    print("Nombre de la función de prueba:", request.function.__name__)

    # Verificando si hay argumentos en la función de prueba
    if hasattr(request.node, "args"):
        print("Argumentos de la función de prueba:", request.node.args)
    else:
        print("La función de prueba no tiene argumentos.")

    # Accediendo al nombre del módulo de la prueba
    print("Módulo de la prueba:", request.module.__name__)

    yield "Datos configurados para la prueba"

    print("\nFinalizando fixture ejemplo_fixture")


# Prueba que utiliza la fixture ejemplo_fixture
def test_ejemplo_prueba(ejemplo_fixture):
    print("\nEjecutando prueba test_ejemplo_prueba")
    assert ejemplo_fixture == "Datos configurados para la prueba"
