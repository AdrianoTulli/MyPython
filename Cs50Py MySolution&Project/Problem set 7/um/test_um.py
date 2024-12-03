from um import count

def test_count():
    assert count('humor') == 0
    assert count('um, UM, Um, uM.') == 4
