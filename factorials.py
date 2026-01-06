def factorial(num):
    # factorial is only defined for integers 0, 1, 2, ...
    if type(num) != int or num < 0:
        return None

    result = 1
    n = num
    while n > 1:
        result *= n
        n -= 1

    return result
