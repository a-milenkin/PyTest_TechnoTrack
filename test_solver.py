#from unittest import TestCase
from solver import division, get_list


def test_float_1():
    assert type(division(3,4)) == float
def test_float_2():
    assert '.' in str(division(3,4))
def test_AttributeError():
    with pytest.raises(AttributeError):
        assert division(3,4).count() >=0


def test_list_1():
    assert type(get_list(3, 4)) == list

def test_list_2():
    assert len(get_list(3, 4)) >= 0

@pytest.mark.parametirze("a,b, expected_results",[(1,2,2),(3,5,2),([6,6],6,3)])
def test_list_3(a,b,expected_results):
    assert len(get_list(a, b)) == expected_results

# test_float_1()
# test_float_2()
# test_list_1()
# test_list_2()
#
#
# test_list_3()
# test_AttributeError()