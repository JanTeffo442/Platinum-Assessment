class TestMath:

    def test_add(x, y):
        a = 10
        b = 60
        return a + b

    def test_subtract(x, y):

        a = 10
        b = 10
        return a - b

    def test_multiply(x, y):
        a = 10
        b = 10
        return a * b

calculate = TestMath()
print(calculate.test_add(y=10))

print(calculate.test_multiply(y=10))
print(calculate.test_subtract(y=10))