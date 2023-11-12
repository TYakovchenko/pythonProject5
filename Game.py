table = [i for i in range(1, 10)]
win_comb = (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
player_1 =input("Введите имя Игрока 1")
player_2 =input("Введите имя Игрока 2")
def draw_table(table):
    print("~~~~~~~~~~~~~")
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print("~~~~~~~~~~~~~")


def take_input(player_hit):
    valid = False
    while not valid:
        player_answer = int(input(("Выбери номер ячейки " + player_hit + "? ")))

        if player_answer >= 1 and player_answer <= 9:
            if str(table[player_answer - 1]) not in "XO":
                table[player_answer - 1] = player_hit
                valid = True
            else:
                print("Эта ячейка занята, попробуй другую")
        else:
            print("Ошибка ввода. Введите число от 1 до 9: ")


def check_win(table):
    win_coord = win_comb
    for num in win_coord:
        if table[num[0]] == table[num[1]] == table[num[2]]:
            return table[num[0]]
    return False


def main(table):
    counter = 0
    win = False
    while not win:
        draw_table(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            tmp = check_win(table)
            if tmp:
                if tmp == "X":
                    tmp == player_1
                else:
                    tmp == player_2
                print(tmp, "Победил!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_table(table)
main(table)