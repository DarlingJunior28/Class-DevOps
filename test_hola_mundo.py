import unittest
from hola_mundo import hola_mundo, despedida

class TestHolaMundo(unittest.TestCase):
    def test_hola_mundo(self):
        # Verificamos que la función retorne "Hola, mundo"
        self.assertEqual(hola_mundo(), "Hola, mundo")

    def test_despedida(self):
        # Verificamos que la función retorne "Adiós, mundo"
        self.assertEqual(despedida(), "Adiós, mundo")

if __name__ == "__main__":
    unittest.main()