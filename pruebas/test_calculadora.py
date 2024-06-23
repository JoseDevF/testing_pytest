from proyecto.main import Calculadora
import pytest

class TestCalculadora:
    @pytest.mark.parametrize("num1, num2, v_esperado",[
        (3,4,7),
        (3.5, 8.2, 11.7),
        (4, 0, 4)
    ])
    def test_sumar(self, num1, num2, v_esperado):
        calculadora=Calculadora()
        resultado = calculadora.sumar(num1,num2)
        assert resultado == v_esperado


    def test_restar(self):
        resultado = Calculadora.restar(10,6)
        assert resultado == 4


    def test_dividir(self):
        resultado = Calculadora.dividir(5,2)
        assert resultado == 2.5




