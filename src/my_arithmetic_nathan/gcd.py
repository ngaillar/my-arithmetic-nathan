"""Calcul du plus grand commun diviseur."""


def gcd(a: int, b: int) -> int:
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd() n'accepte que des entiers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

   # gitlab-runner register  --url https://gitlab.univ-lr.fr  --token glrt-f_5WfCPjs3mH5X_7d4LhOW86MQpwOjl6awp0OjMKdToxdmET.01.1c18jsr44
   git@gitlab.univ-lr.fr:ngaillar/my-arithmetic-nathan.git