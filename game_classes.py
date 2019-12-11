import random
from numbers_checks import check_number_in_list
from numbers_checks import check_number_in_column
from numbers_checks import check_number_in_row


class Card:
    def __init__(self):
        self.counter = 0
        row_1 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        row_2 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        row_3 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.card = [row_1, row_2, row_3]
        self.selected_numbers = []
        for i in range(3):
            each_row = []
            column = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            while len(self.selected_numbers) < 15:
                number = random.randint(1, 90)
                if check_number_in_list(number, self.selected_numbers):
                    if check_number_in_column(number, column):
                        position = number // 10
                        if number == 90:
                            position = 8
                        column[position] += 1
                        if check_number_in_row(number, each_row):
                            self.selected_numbers.append(number)
                            each_row.append(number)
                        else:
                            break
                else:
                    continue

            self.selected_numbers.sort()
            each_row.sort()

            for each in each_row:
                each_position = each // 10
                if each == 90:
                    each_position = 8
                self.card[i][each_position] = each

    def print_card(self, player):
        print('---- Карточка', player, '------')
        for i in range(3):
            print(*self.card[i])
        print('-' * 30)

    def check_number_in_card(self, number, player):
        for i in range(3):
            if number in self.card[i]:
                self.counter += 1
                if self.counter == 15:
                    print('Карточка', player, 'выграла!!!!')
                    exit()
                position = self.card[i].index(number)
                if number > 9:
                    self.card[i][position] = ' -'
                else:
                    self.card[i][position] = '-'

    def __str__(self):
        return f'{len(self.selected_numbers)} numbers in card: {self.selected_numbers}'

    def __getitem__(self, item):
        return self.card[item]

    def __eq__(self, other):
        return self.counter == other.counter

    def __contains__(self, item):
        return item in self.selected_numbers


class Human:
    def __init__(self, name):
        self.name = name
        self.player_card = Card()

    def ask_question(self, number):
        question = input('Зачеркнуть цифру? (y/n) ')
        if question == 'y' and number in self.player_card.selected_numbers:
            self.player_card.check_number_in_card(number, self.name)
        elif question == 'y' and number not in self.player_card.selected_numbers:
            print('числа нет на карточке - человек проиграл')
            exit()
        elif question == 'n' and number in self.player_card.selected_numbers:
            print('число есть на карточке - человек проиграл')
            exit()
        else:
            return

    def __str__(self):
        return f'Y {self.name} {self.player_card}'

    def __eq__(self, other):
        return self.player_card == other.player_card


class Computer(Human):
    def __init__(self, name):
        self.name = 'компьютера #' + str(name)
        self.player_card = Card()

    def ask_question(self, number):
        self.player_card.check_number_in_card(number, self.name)
        self.player_card.print_card(self.name)

    def __str__(self):
        return f'У {self.name} {self.player_card}'

    def __eq__(self, other):
        return self.player_card == other.player_card


if __name__ == '__main__':
    new_card = Card()
    print(new_card)
    print(90 in new_card)

    second_card = Card()
    print(second_card)
    print(90 in new_card)
    for row in second_card:
        print(*row)

    print(new_card == second_card)

    man = Human('Leo')
    print(man)
    print(90 in man.player_card)

    second_man = Human('Kate')
    print(second_man)
    print(90 in man.player_card)
    print(man == second_man)

    comp = Computer('1')
    print(comp)
