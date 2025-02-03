def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def reverse(n):
    return int(str(n)[::-1])
