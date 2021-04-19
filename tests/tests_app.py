import sys
from unittest import TestCase, main

sys.path.append(r"D:\Python\cifra_cesar")
from src.app import decrypt, encrypt  # NOQA


class TestCifraCesar(TestCase):
    def test_encrypt_deve_retornar_def_quando_entrar_abc(self):
        entrada = "abc"
        saida = "def"
        self.assertEqual(encrypt(entrada), saida)

    def test_encrypt_deve_retornar_abc_quando_entrar_xyz(self):
        entrada = "xyz"
        saida = "abc"
        self.assertEqual(encrypt(entrada), saida)

    def test_decrypt_deve_retornar_abc_quando_entrar_def(self):
        entrada = "def"
        saida = "abc"
        self.assertEqual(decrypt(entrada), saida)

    def test_decrypt_deve_retornar_xyz_quando_entrar_abc(self):
        entrada = "abc"
        saida = "xyz"
        self.assertEqual(decrypt(entrada), saida)


if __name__ == "__main__":

    main()
