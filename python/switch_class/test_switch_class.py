import pytest
from switch_class import switch_class

def test_initialize():
    default = 'not found'
    myswitch = switch_class.switch(default)
    assert myswitch.default_return_value == default
