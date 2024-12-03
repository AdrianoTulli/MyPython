import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11 PM to 5 AM") == "23:00 to 05:00"
    assert convert("9:00 PM to 5:55 AM") == "21:00 to 05:55"

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def main():
    test_convert()
