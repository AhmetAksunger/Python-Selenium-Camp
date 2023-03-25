
#Week 5 Homework 1 - Pytest Decorators

Pytest decorators are often used to mark functions as test cases or to modify the behavior of the tests.

Some popular Pytest decorators would be:


## @pytest.mark.parametrize()

This pytest command helps you test multiple inputs in one test function. The use of this command would be like this:

```
@pytest.mark.parametrize("string1,string2",[("test","test"),("a","a"),("a","c")])

def test_stringsEqual(string1,string2):
    assert string1 == string2
```

## @pytest.mark.skip

Skips the test.

```
@pytest.mark.skip(reason="You can enter the reason here")
def test_skip():
    assert True
```

## @pytest.mark.skipif()
Skips the test if the condition after it is true.

@pytest.mark.skipif(sys.platform != 'linux', reason="Linux tests")
def test_linux():
    assert True

## @pytest.mark.xfail
If you're expecting a test to fail, you can use this decorator.
It marks the test as "excpected fail" , if the test actually fails it will say "excpected fail".

```
@pytest.mark.xfail
def test_something():
    assert False
```
## @pytest.mark.timeout()
It's like WebDriverWait in selenium. It basically assigns a maximum time for a test to take, if it takes longer than that it fails.

```
@pytest.mark.timeout(5)
def test_something():
    assert True
```