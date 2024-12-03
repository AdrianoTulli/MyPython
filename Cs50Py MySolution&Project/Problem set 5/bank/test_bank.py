from bank import value

def test_zero() :
    assert value("hello") == 0
    assert value("HELLO0,!") == 0

def test_twenty ():
    assert value('hy') == 20
    assert value('HY1,!') == 20

def test_hundred() :
    assert value('Ciao.!1') == 100
