import pytest
import sys
import ipdb

# Simple fixture
class Container(object):
    def __init__(self):
        self.a = None
        self.b = None
        print('Container created')

@pytest.fixture(scope='module')
def mycontainer():
    c = Container()
    c.a = 1
    c.b = 2
    return c

def test_sum(mycontainer):
    x = mycontainer.a + mycontainer.b
    assert x == 3

def test_product(mycontainer):
    x = mycontainer.a * mycontainer.b
    assert x == 2

# Parametrized fixture
@pytest.fixture(scope='module', params=[(1, 2), (3, 4)])
def numbers(request):
    num = {'a': request.param[0],
           'b': request.param[1]
           }
    return num

def add_numbers(a, b):
    return a + b

def test_add_numbers(numbers):
    expected =  numbers['a'] + numbers['b']
    actual = add_numbers(numbers['a'], numbers['b'])
    assert actual == expected

# Multiple fixtures
@pytest.fixture(params=[1, 2, 3])
def num_a(request):
    return request.param

@pytest.fixture(params=[10, 20])
def num_b(request):
    return request.param

def test_add_numbers2(num_a, num_b):
    actual = add_numbers(num_a, num_b)
    expected = num_a + num_b
    assert actual == expected


def test_write(tmpdir):
    f = tmpdir.join('file.txt')
    f.write('Hello world')
    print(f)
    ipdb.set_trace()


# temporary file that will be removed
@pytest.fixture
def tmp_file(request, tmpdir):
    f = str(tmpdir.join('file.h5'))
    def tear_down():
        os.remove(f)
    request.addfinalizer(tear_down)
    return f
