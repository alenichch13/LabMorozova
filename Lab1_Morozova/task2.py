# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
pages = 100
lines = 50
symbols = 25
symbol1 = 4

quantity = int(volume * 1024 * 1024/ (pages * lines * symbols * symbol1))

print("Количество книг, помещающихся на дискету:", quantity)