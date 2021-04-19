from functools import partial
from operator import mod
from string import ascii_lowercase as alpha

t = len(alpha)


def calc(letra, tipo="encrypt"):
    """
    Calculates expression to encrypt and decrypt.
    :param letra: input string.
    :param tipo: string type.
    :return: expression.
    """
    if tipo == "encrypt":
        exp = alpha.index(letra) + 3
    else:
        exp = alpha.index(letra) - 3
    return alpha[mod(exp, t)]


def encrypt(frase: str) -> str:
    """
    Encryption method.
    :param frase: input string.
    :return: encrypted string.
    """
    return "".join(map(calc, frase))


dec = partial(calc, tipo="decrypt")


def decrypt(frase: str) -> str:
    """
    Decrypt method.
    :param frase: input string.
    :return: decrypted string.
    """
    return "".join(map(dec, frase))
