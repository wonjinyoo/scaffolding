# scaffolding
 
1) create `Makefile`

```makefile
install:
    pip install --upgrade pip
    pip install -r requirements.txt

install-gcp:
    pip install --upgrade pip
    pip install -r requirements-gcp.txt

install-aws:
    pip install --upgrade pip
    pip install -r requirements-aws.txt

install-amazon-linux:
    pip install --upgrade pip
    pip install -r amazon-linux.txt

lint:
    pylint --disable=R,C hello.py

format:
    black *.py

test:
    python -m pytest -vv --cov=hello test_hello.py
```

2) create `requirements.txt`

```
pytest
click
pylint
pytest-cov
```

3)  create `hello.py`, `test_hello.py`

```python
def add(x, y):
    """This is an Add Function"""
    return x + y

print(add(2, 5))
```

```python
from hello import add

# add 함수를 test하는 function
def test_add():
    assert 7 == add(2, 5)
```

**4) CI- virtual environment creation**

```python
# cmd
python -m venv demo   # demo라는 이름의 가상환경 생성
demo\Scripts\activate.bat   # 가상환경 활성화

(demo) C:\Users\splen\Desktop\scaffolding\scaffolding>pip install -r requirements.txt
(demo) C:\Users\splen\Desktop\scaffolding\scaffolding>pylint --disable=R,C hello.py

------------------------------------
Your code has been rated at 10.00/10

(demo) C:\Users\splen\Desktop\scaffolding\scaffolding>python -m pytest -vv --cov=hello test_hello.py
test_hello.py::test_add PASSED                                                                                                                                            [100%] 

---------- coverage: platform win32, python 3.10.5-final-0 -----------
Name       Stmts   Miss  Cover
------------------------------
hello.py       3      0   100%
------------------------------
TOTAL          3      0   100%
============================================================================== 1 passed in 0.19s ===============================================================================

deactivate   # 가상환경 끄기
```
