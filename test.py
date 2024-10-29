import main as mn

def test_fibonacci():
    fibonacci = mn.fibonacci(5)
    assert fibonacci == [0, 1, 1, 2, 3]


def test_min():
    resultado = mn.get_min([1, 2, 3, 4, 5])
    assert resultado == 1


def test_min2():
    resultado2 = mn.get_min([1, 2, -3, 4, 5, 12])
    assert resultado2 == -3


def test_max():
    resultado = mn.get_max([1, 2, 3, 4, 5])
    assert resultado == 5

def test_max2():
    resultado2 = mn.get_max([1, 2, -3, 4, 5, 12])
    assert resultado2 == 12

def test_comun():
    comunes = mn.get_comun([1, 2, -3, 4, 5, 12],[1, 2, 3, 4, 5])
    assert comunes == [1,2,4,5]
def test_areaMax():
    areaM=mn.area_max([1,8,6,2,5,4,8,3,7])
    assert  areaM == 49
