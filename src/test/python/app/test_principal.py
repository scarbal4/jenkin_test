import unittest
from src.main.python.model.principal import *


class TestDataPreparation(unittest.TestCase):

    def test_init(self):
        animal="gato_test"
        nombre_animal="misifu_test"
        sonido_emitido="maullido_test"
        gato=mascota(animal, nombre_animal, sonido_emitido)

    def test_MiFuncion_Arranque(self):
        MiFuncion_Arranque()



if __name__ == "__main__":
    unittest.main()