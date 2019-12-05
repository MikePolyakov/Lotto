import unittest
from game_classes import Human, Computer


class TestHuman(unittest.TestCase):
    def test_init(self):
        player = Human()
        self.assertEqual(player.name, 'человека')


class TestComputer(unittest.TestCase):
    def test_init(self):
        player = Computer()
        self.assertEqual(player.name, 'компьютера')
