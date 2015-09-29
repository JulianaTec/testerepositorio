from unittest import TestCase

# Importa o controlador que será testado
import default

__author__ = 'TecSUS-3'


class TestIndex(TestCase):
    def test_index(self):
        self.assertEqual(default.index()['nome'],'blai')
        self.fail()