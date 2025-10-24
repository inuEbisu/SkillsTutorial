def f(n: int) -> int:
    return 1 if n <= 1 else f(n - 1) + g(n - 2)


def g(n: int) -> int:
    return 1 if n <= 1 else f(n - 1) + g(n - 1)
