field=[["-"] * 3 for i in range(3)]

def show_field():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

def ty_hodish():
    while True:
        coords_ = input("Введи координаты: ").split()
        if len(coords_) != 2:
            print("Введи две координаты!")
            continue
        x, y = coords_

        if not(x.isdigit()) or not(y.isdigit):
            print("Введи числа!")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 and 0 > y or y > 2:
            print("Введи координаты в диапазоне от 0 до 2!")
            continue

        if field[x][y] != "-":
            print("Клетка занята! Выбери другую")
            continue
        return x, y

def pobeds():
    pobeds_coords_=[((0, 0), (1, 1), (2, 2)),
                 ((2, 0), (1, 1), (0, 2)),
                 ((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (1, 2)),
                 ((0, 2), (1, 2), (2, 2))]
    if field[0][0] == field[1][1] == field[2][2] != "-" or \
            field[2][0] == field[1][1] == field[0][2] != "-" or \
            field[0][0] == field[0][1] == field[0][2] != "-" or \
            field[1][0] == field[1][1] == field[1][2] != "-" or \
            field[2][0] == field[2][1] == field[2][2] != "-" or \
            field[0][0] == field[1][0] == field[2][0] != "-" or \
            field[0][1] == field[1][1] == field[1][2] != "-" or \
            field[0][2] == field[1][2] == field[2][2] != "-":

                print("Игра окончена")
                return True

    return False


print("")
print("Крестики-нолики")
print("Выигрывает игрок, первый собравший три символа в ряд")
print("по горизонтали, вертикали или диагонали")

num = 0
while True:
    num += 1
    show_field()
    if num % 2 == 1:
        print("Ходит Х")
    else: print("Ходит O")

    x, y = ty_hodish()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if pobeds():
        show_field()
        break

    if num == 9:
        show_field()
        print("Ничья")
        break








