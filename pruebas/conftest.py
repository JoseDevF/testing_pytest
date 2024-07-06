#Este archivo permite "registrar" fixtures
# para su uso en cualquier test y archivo.

pytest_plugins = [
    "pruebas.fixtures.BaseDeDatos",
    "pruebas.fixtures.UseFixturesExample"
]