import pytest
from calculadora import sumar, dividir

def test_sumar_basico():
    # Esta prueba verifica que 2 + 3 sea 5
    assert sumar(2, 3) == 5

def test_dividir_por_cero():
    # Esta prueba verifica que el programa detecte el error de dividir por cero
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
        