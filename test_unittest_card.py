import unittest
from game_classes import Card


class TestCard(unittest.TestCase):
    def test_init(self):
        test_card = Card()
        self.assertEqual(test_card.counter, 0)
        self.assertEqual(len(test_card.selected_numbers), 15)
        self.assertEqual(len(test_card.card), 3)

    def test_print_card(self):
        test_card = Card()
        player = '#1'
        print()
        test_card.print_card(player)
        self.assertEqual(player, '#1')

    def test_check_number_in_card(self):
        test_card = Card()
        number = 90
        player = '#1'
        test_card.check_number_in_card(number, player)
        self.assertEqual(test_card.counter, 0)

    def test_str(self):
        new_card = Card()
        test_card = f'{len(new_card.selected_numbers)} numbers in card: {new_card.selected_numbers}'
        assert test_card == str(new_card)
