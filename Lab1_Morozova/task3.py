list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
quantity_pl = len(list_players)
quantity_team = quantity_pl//2

players_1 = list_players[:quantity_team]
players_2 = list_players[quantity_team:]
print(players_1)
print(players_2)


