import pytest


@pytest.mark.parametrize("a,b,c",[(10,3,5),(12,2,2)])
def test_addition(a,b,c):
    w=a+b+c
    print(w)





