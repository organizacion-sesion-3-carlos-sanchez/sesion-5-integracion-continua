# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import is_even

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación is_even
    def test_is_even(self):
        assert is_even(4) == True
        assert is_even(3) == False
        assert is_even(-1) == False
        assert is_even(0) == True
