from string import ascii_lowercase as alpha
from operator import mod
from functools import partial


t = len(alpha)


def calc(letra, tipo="encrypt"):
    if tipo == "encrypt":
        exp = alpha.index(letra) + 3
    else:
        exp = alpha.index(letra) - 3
    return alpha[mod(exp, t)]


def encrypt(frase: str) -> str:
    return "".join(map(calc, frase))


dec = partial(calc, tipo="decrypt")


def decrypt(frase: str) -> str:
    return "".join(map(dec, frase))
