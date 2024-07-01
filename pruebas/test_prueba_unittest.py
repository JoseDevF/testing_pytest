import unittest

class TestPrueba(unittest.TestCase):

    #1 - Arrange o setup
    def setUp(self) -> None:
        print("""
        #1 - Configurando el entorno de los test
        - Se creo el carrito de compras vacío - OK
        """)


    def test_agregar_producto(self):
        print("""
        #2 - Código necesario para agregar el producto al carrito de compras
        """)
        print("### añadiendo el producto")
        assert False #3 - Assert o evaluación
        print("### Añadido con éxito - OK")

    # 4 - Cleanup o limpieza
    def tearDown(self):
        print("""
        #4 - Se estan eliminando todos los productos del carrito
        """)