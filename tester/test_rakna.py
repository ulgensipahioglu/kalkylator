import pytest
from kalkylator.rakna import addera, subtrahera, multiplicera, dividera, upphoja


class TestAddera:

    def test_positiva_tal(self):
        assert addera(2, 3) == 5

    def test_negativa_tal(self):
        assert addera(-1, -1) == -2

    def test_noll(self):
        assert addera(0, 5) == 5


class TestSubtrahera:

    def test_enkelt(self):
        assert subtrahera(10, 3) == 7

    def test_negativt_resultat(self):
        assert subtrahera(3, 10) == -7


class TestMultiplicera:

    def test_enkelt(self):
        assert multiplicera(4, 5) == 20

    def test_med_noll(self):
        assert multiplicera(100, 0) == 0


class TestDividera:

    def test_enkelt(self):
        assert dividera(10, 2) == 5.0

    def test_division_med_noll(self):
        with pytest.raises(ValueError):
            dividera(5, 0)


class TestUpphoja:

    def test_enkelt(self):
        assert upphoja(2, 3) == 8

    def test_noll_exponent(self):
        assert upphoja(5, 0) == 1

    def test_negativ_exponent(self):
        assert upphoja(2, -1) == 0.5
