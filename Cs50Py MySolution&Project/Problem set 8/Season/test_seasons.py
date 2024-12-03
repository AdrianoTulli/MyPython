import pytest
from seasons import def_user_input
from unittest.mock import patch

#I'll simulate the input using mocking
def test_def_user_input_valid():
    with patch('builtins.input', return_value='1999-11-18'):
        assert def_user_input() == '1999-11-18'

def test_def_user_input_invalid():
    with patch('builtins.input', return_value='a£0d%-,34-£0'):
        with pytest.raises(SystemExit):
            def_user_input()
