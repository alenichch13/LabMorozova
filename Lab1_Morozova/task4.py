users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

quantity = len(users)
uniq_quantity = len(set(users))

visits["Общее количество"] = quantity
visits["Уникальные посещения"] = uniq_quantity

print(visits)