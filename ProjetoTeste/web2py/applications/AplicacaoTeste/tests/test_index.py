from unittest import TestCase

# Importa o controlador que sera testado
import os,sys

print '>>>>',os.path.dirname(__file__)
print '>>>>',sys.path

import default

__author__ = 'TecSUS-3'


class TestIndex(TestCase):
    def test_index(self):
        self.assertEqual(default.index()['nome'],'blai')
      
