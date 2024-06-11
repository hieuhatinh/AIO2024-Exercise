def factorial(n):
    result_factorial = 1

    for i in range(1, n+1):
        result_factorial *= i
    return result_factorial


def valid_garther_zero(n):
    return n > 0


def approximate_sin(x, n):
    result = 0
    for i in range(n):
        result_item = (-1)**i * (x**(2*i + 1) / factorial(2*i + 1))
        result += result_item
    return result


def approximate_cos(x, n):
    result = 0
    for i in range(n):
        result_item = (-1)**i * (x**(2*i) / factorial(2*i))
        result += result_item
    return result


def approximate_sinh(x, n):
    result = 0
    for i in range(n):
        result_item = x**(2*i + 1) / factorial(2*i + 1)
        result += result_item
    return result


def approximate_cosh(x, n):
    result = 0
    for i in range(n):
        result_item = x**(2*i) / factorial(2*i)
        result += result_item
    return result


def approximate_functions(x, n):
    try:
        if not valid_garther_zero(n):
            raise ValueError('n phải lớn hơn 0')

        print(approximate_sin(x, n))
        print(approximate_cos(x, n))
        print(approximate_sinh(x, n))
        print(approximate_cosh(x, n))
    except Exception as e:
        print(e)
        return


approximate_functions(x=3.14, n=10)
