import random
from game_classes import Human
from game_classes import Computer


def man_or_comp(i, comp_number):
    type_of_player = input(f'игрок №{i+1} - это человек?  (y/n) ')
    if type_of_player == 'y':
        name = input('What is his name? ')
        return Human(name)
    else:
        comp_number += 1
        return Computer(comp_number)


number_of_players = int(input('Сколько будет игроков в игре лото? '))
lotto_players = []
computer_number = 0
for i in range(number_of_players):
    lotto_player = man_or_comp(i, computer_number)
    if lotto_player.name[-1:].isdigit():
        computer_number = int(lotto_player.name[-1:])
    lotto_players.append(lotto_player)
print('=' * 30)
print('Игра начинается')

for i in range(number_of_players):
    lotto_players[i].player_card.print_card(lotto_players[i].name)

barrel_list = []
while True:
    new_barrel = random.randint(1, 90)
    if new_barrel not in barrel_list:
        barrel_list.append(new_barrel)
        barrel_list.sort()
    else:
        continue

    print('Новый бочонок:', new_barrel, 'осталось:', 90 - len(barrel_list))
    for i in range(number_of_players):
        if lotto_players[i].name[-1:].isdigit():
            lotto_players[i].ask_question(new_barrel)
        else:
            lotto_players[i].player_card.print_card(lotto_players[i].name)
            lotto_players[i].ask_question(new_barrel)
