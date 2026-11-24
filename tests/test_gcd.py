import math

import pytest

from my_arithmetic_nathan import gcd


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (12, 18, 6),
        (18, 12, 6),      # commutativité
        (17, 5, 1),       # nombres premiers entre eux
        (7, 7, 7),        # nombres égaux
        (0, 5, 5),        # un argument nul
        (5, 0, 5),
        (0, 0, 0),
        (-12, 18, 6),     # nombres négatifs
        (12, -18, 6),
        (-12, -18, 6),
        (1, 1000, 1),
    ],
)
def test_gcd_values(a, b, expected):
    assert gcd(a, b) == expected


def test_gcd_matches_math_gcd():
    for a in range(-30, 31):
        for b in range(-30, 31):
            assert gcd(a, b) == math.gcd(a, b)


@pytest.mark.parametrize(("a", "b"), [(1.5, 2), (2, "3"), (None, 1)])
def test_gcd_rejects_non_integers(a, b):
    with pytest.raises(TypeError):
        gcd(a, b)