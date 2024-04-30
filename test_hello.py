from hello import add

# add 함수를 test하는 function
def test_add():
    assert 7 == add(2, 5)