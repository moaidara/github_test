from src.calcul import addition, multiplication
from src.message import bonjour


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0


def test_multiplication():
    assert multiplication(2, 4) == 8
    assert multiplication(0, 10) == 0


def test_bonjour():
    assert bonjour("Ghost") == "Bonjour, Ghost !"
