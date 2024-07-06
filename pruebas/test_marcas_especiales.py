import pytest
import sys

@pytest.mark.skip("Este test no se ejecuta en 24 horas start 09:38")
def test_prueba():
    assert False


def verificar_EV():
    return False


@pytest.mark.skipif(condition=verificar_EV() != False, reason="Variables de entorno no encontradas")
def test_prueba2():
    assert True


@pytest.mark.skipif(condition=sys.platform=="win32", reason="Variables de entorno no encontradas")
def test_prueba3():
    assert True


#Ejemplo para diferenciar skipIf y XFail.

# función a probar
def dividir(a, b):
    return a / b


@pytest.mark.skipif(sys.platform == "win64", reason="No se ejecuta en Windows")
def test_dividir():
    assert dividir(10, 2) == 5


@pytest.mark.xfail(raises=ZeroDivisionError, reason="Conocido bug con la división por cero")
def test_dividir_por_cero():
    assert dividir(10, 0) == "esto no se alcanza"
