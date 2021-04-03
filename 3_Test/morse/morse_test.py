import pytest
import morse
import flake8


@pytest.mark.parametrize('i,exp', [
    ('... --- ...', 'SOS'),
    ('.--. .. -. -.-. ....', 'PINCH'),
    ('..- -. .. -', 'UNIT'),
    ('.. .- -- --. .-. --- --- -',
     'IAMGROOT')
])
def test_decode(i, exp):
    assert morse.decode(i) == exp
