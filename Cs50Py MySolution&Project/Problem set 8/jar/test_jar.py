from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(6)
    assert jar.capacity == 6

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
