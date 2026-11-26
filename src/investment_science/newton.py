from typing import Callable


def newtons_method(
    f: Callable[[float], float], f_p: Callable[[float], float], lambda_k: float
) -> float:
    """Return the next estimate of a root of f, given its derivative f_p."""
    return lambda_k - (f(lambda_k) / f_p(lambda_k))


def newton_iterates(
    f: Callable[[float], float], f_p: Callable[[float], float], lambda_0: float, n: int
) -> list[float]:
    """Return the initial estimate lambda_0 followed by n Newton iterates."""
    lambdas = [lambda_0]
    for k in range(1, n + 1):
        lambdas.append(newtons_method(f, f_p, lambdas[k - 1]))

    return lambdas
