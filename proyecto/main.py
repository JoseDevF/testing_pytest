class Calculadora:

    def sumar(self, a:int, b:int) -> float:
        return a+b

    @classmethod
    def restar(cls, a: int, b:int) -> float:
        return a-b

    @staticmethod
    def dividir(a: int, b:int) -> float:
        return a/b

