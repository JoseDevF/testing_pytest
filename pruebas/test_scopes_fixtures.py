# test_calculadora.py
import pytest

# Fixture para configurar datos antes de cada prueba
@pytest.fixture(scope="function")
def configurar_datos():
    datos = {"a": 5, "b": 3}  # Datos de ejemplo
    print("\nConfigurando datos antes de la prueba")
    yield datos  # El yield permite retornar los datos y seguir después de la prueba
    print("\nLimpiando datos después de la prueba")
    # Aquí podrías agregar código para limpiar los datos si es necesario

# Prueba simple usando la fixture configurar_datos
def test_suma(configurar_datos):
    resultado = sumar(configurar_datos["a"], configurar_datos["b"])
    assert resultado == 8

# Función a probar
def sumar(a, b):
    return a + b
