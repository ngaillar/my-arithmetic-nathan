"""Calcul du plus grand commun diviseur."""


def gcd(a: int, b: int) -> int:
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd() n'accepte que des entiers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a