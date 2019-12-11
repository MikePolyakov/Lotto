import unittest
from game_classes import Human, Computer


class TestHuman(unittest.TestCase):
    def test_init(self):
        player = Human('человека')
        self.assertEqual(player.name, 'человека')

    def test_str(self):
        man = Human('human')
        test_player = f'Y {man.name} {man.player_card}'
        assert test_player == str(man)


class TestComputer(unittest.TestCase):
    def test_init(self):
        player = Computer('1')
        self.assertEqual(player.name, 'компьютера #1')

    def test_str(self):
        comp = Computer('1')
        test_player = f'Y {comp.name} {comp.player_card}'
        assert test_player == str(comp)

