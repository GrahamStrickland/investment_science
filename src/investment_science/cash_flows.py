from typing import Sequence

from investment_science.newton import newton_iterates


def growth_factor(r: float, n: int) -> float:
    """Return the growth of one unit after n periods at a rate r per period."""
    return (1 + r) ** n


def present_value(xs: Sequence[float], r: float) -> float:
    """Return the present value of the cash flow stream xs at a rate r per period."""
    return sum(xs[k] / (1 + r) ** k for k in range(len(xs)))


def present_value_p(xs: Sequence[float], r: float) -> float:
    """Return the derivative with respect to r of the present value of xs."""
    return sum(-k * xs[k] / (1 + r) ** (k + 1) for k in range(1, len(xs)))


def irr_iterates(xs: Sequence[float], r_0: float, n: int) -> list[float]:
    """Return n Newton iterates, starting from r_0, for the internal rate of
    return of the cash flow stream xs."""
    return newton_iterates(
        lambda r: present_value(xs, r), lambda r: present_value_p(xs, r), r_0, n
    )
