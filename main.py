import random
import time


class Game:
    def __init__(self):
        self.row_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        self.col_index = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}

    def input_(self, txt):
        row_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        col_index = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        while True:
            try:
                inp = input(txt)
                if len(inp) == 2:
                    inp = [inp[0], inp[1]]
                else:
                    inp = inp.strip().split()
                if len(inp) == 2 and len(inp[0]) == 1 and len(inp[1]) == 1:
                    row = row_index[inp[0]]
                    col = col_index[inp[1]]

                    return row, col
                else:
                    raise Exception(self.error_input)

            except Exception as ex:
                print(f"Ошибка ввода. Используйте следующие форматы 'a1' 'a 1'\nПопробуйте еще раз...")


class Persone(Game):
    def __init__(self, name="AI"):
        self.user_matrix = [["O" for i in range(6)] for i in range(6)]
        self.user_name = name

    def show_map(self, m=False, sheeps=False, hidden=False, get=False):
        if not m: m = self.user_matrix.copy()
        else: m = m.copy()
        if hidden:
            m = [[i.replace("■", "O").replace("t", "O") for i in r] for r in m]
        if get:
            return m
        if sheeps:
            s = ["■ "*i for i in sheeps]
            if 6-len(sheeps) > 0:
                for i in range(6-len(sheeps)):
                    s.append(" ")
        else:
            s = [" " for i in range(6)]
        print("    1  2  3  4  5  6", end="\n")
        print(f" a  {m[0][0]}  {m[0][1]}  {m[0][2]}  {m[0][3]}  {m[0][4]}  {m[0][5]}     {s[0]}", end="\n")
        print(f" b  {m[1][0]}  {m[1][1]}  {m[1][2]}  {m[1][3]}  {m[1][4]}  {m[1][5]}     {s[1]}", end="\n")
        print(f" c  {m[2][0]}  {m[2][1]}  {m[2][2]}  {m[2][3]}  {m[2][4]}  {m[2][5]}     {s[2]}", end="\n")
        print(f" d  {m[3][0]}  {m[3][1]}  {m[3][2]}  {m[3][3]}  {m[3][4]}  {m[3][5]}     {s[3]}", end="\n")
        print(f" e  {m[4][0]}  {m[4][1]}  {m[4][2]}  {m[4][3]}  {m[4][4]}  {m[4][5]}     {s[4]}", end="\n")
        print(f" f  {m[5][0]}  {m[5][1]}  {m[5][2]}  {m[5][3]}  {m[5][4]}  {m[5][5]}     {s[5]}", end="\n")

    def creat_sheep(self, sheeps, test=False, rand=True):
        sh = sheeps.copy()
        if not test:
            for sheep in sheeps:
                m = self.user_matrix
                sheep_coords = []
                for corpus in range(sheep):
                    while True:

                        try:
                            print("\n"*50)
                            self.show_map(sheeps=sh)
                            r, c = self.input_(f"Введите координаты {corpus+1} палубы {sheep}х палубного корабля: ")
                            if m[r][c] == "■":
                                #
                                raise Exception("Здесь уже есть корабля")
                            for ir, ic in [[-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1],[1,0],[1,1]]:
                                rr, cc = r + ir, c + ic
                                if 6 > rr > -1 and 6 > cc > -1:
                                    if m[rr][cc] == "■":
                                        raise Exception("Вы не можете ставить корабль вплотную к другому кораблю. Расстояние между кораблями должно быть миниммум одна клетка!")
                            if sheep_coords:
                                lr, lc = sheep_coords[-1]
                                if abs(lr-r) > 1 or abs(lc-c) > 1:
                                    raise Exception("The ship must be monolithic")
                                elif abs(lr-r) == 0 and abs(lc-c) == 0:
                                    raise Exception("Вертикальный корабль - убитый корабль =). Поставьте корабль в одну линию")
                        except Exception as ex:
                            print("Ошибка при создании корабля - ", ex)
                        else:
                            break
                        time.sleep(4)

                    sheep_coords.append([r, c])
                sh.pop(0)

                # CREATED SHEEP
                for r, c in sheep_coords:
                    m[r][c] = "■"
        elif rand:
            sheep_coords = [
                [[0,0],[0,1],[0,2], [0,4],[0,5], [2,0],[2,1], [2,3], [2,5], [4,0], [5,5]],
                [[0,2],[0,3],[0,4], [0,0],[1,0], [5,0],[5,1], [5,3], [5,5], [3,3], [2,5]],
                [[0,2],[1,2],[2,2], [1,4],[1,5], [1,0],[2,0], [4,0], [4,2], [5,4], [3,5]],
                [[3,5],[4,5],[5,5], [0,5],[1,5], [5,2],[5,3], [5,0], [3,0], [1,0], [0,3]],
                [[4,1],[4,2],[4,3], [0,4],[0,5], [2,0],[2,1], [2,3], [2,5], [0,1], [5,5]],
                [[3,0],[4,0],[5,0], [2,2],[2,3], [5,2],[5,3], [0,0], [0,4], [4,5], [2,5]]
            ]

            m = self.user_matrix
            # CREATED SHEEP
            for r, c in random.choice(sheep_coords):
                m[r][c] = "■"
        else:
            sheep_coords = [[0,0],[0,1],[0,2], [0,4],[0,5], [2,0],[2,1], [2,3], [2,5], [4,0], [5,5]]
            m = self.user_matrix

            # CREATED SHEEP
            for r, c in sheep_coords:
                m[r][c] = "■"

        print("Корабли созданы.")

    def shoot(self, ai=False, contr_user_name=""):
        m = self.user_matrix
        self.show_map(hidden=True)
        while True:
            if ai:
                r, c = self.ai()
            else:
                r, c = self.input_("Стреляй!: ")
            print('\n' * 40)
            mm = m[r][c]
            shoot = False
            if mm == "■":
                m[r][c] = "x"
                for ir, ic in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    rr, cc = r + ir, c + ic
                    if 6 > rr > -1 and 6 > cc > -1:
                        if m[rr][cc] == "■":
                            print("\nРанил. Стреляй еще!")
                            shoot = True
                            self.show_map(hidden=True)
                            break
                for ir, ic in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    rr, cc = r + ir, c + ic
                    if 6 > rr > -1 and 6 > cc > -1:
                        if m[rr][cc] == "x":
                            for ir2, ic2 in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                                rr2, cc2 = rr + ir2, cc + ic2
                                if 6 > rr2 > -1 and 6 > cc2 > -1:
                                    if m[rr2][cc2] == "■":
                                        print("\nРанил. Стреляй еще!")
                                        shoot = True
                                        self.show_map(hidden=True)
                                        break
                if not shoot:
                    for ir, ic in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                        rr, cc = r + ir, c + ic
                        if 6 > rr > -1 and 6 > cc > -1:
                            if m[rr][cc] != "x":

                                for r1, row in enumerate(m):
                                    for c1, i in enumerate(row):
                                        if i == "x":
                                            m[r1][c1] = m[r1][c1].upper()
                                            for ir2, ic2 in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0],
                                                           [1, 1]]:
                                                if 6 > r1+ir2 > -1 and 6 > c1+ic2 > -1:
                                                    if m[r1 + ir2][c1 + ic2] == "O":
                                                        m[r1 + ir2][c1 + ic2] = "t"

                    if self.if_win():
                        print(contr_user_name,"Победил")
                        time.sleep(5)
                        exit()


                    print("\nКорабль убит. Стреляй снова.")
                    self.show_map(hidden=True)
            elif mm == "O":
                m[r][c] = "T"
                print("Не попал")
                self.show_map(hidden=True)
                time.sleep(3)
                break
            elif mm in ["x", "X", "T"]:
                print("Вы уже стреляли сюда")
            elif mm == "t":
                m[r][c] = "T"
                print("Мимо. Запомните - расстояние между короблями = 1 клетка")
                self.show_map(hidden=True)
                time.sleep(3)
                break

    def ai(self):
        m = self.show_map(hidden=True, get=True)
        print("Подождите, я думаю ", end="")
        for i in range(4):
            time.sleep(1)
            print('.', end=' ')
        around, around2 = [], []
        for r, row in enumerate(m):
            for c, i in enumerate(row):
                if i == "x":
                    [around.append([r+r1, c+c1]) for r1, c1 in [[-1,0],[0,1],[1,0],[0,-1]] if 6 > r+r1 > -1 and 6 > c+c1 > -1 and m[r+r1][c+c1] != "T" and m[r+r1][c+c1] != "t" and m[r+r1][c+c1] != "x"]
                    [around2.append([r-r1, c-c1]) for r1, c1 in [[-1,0],[0,1],[1,0],[0,-1]] if 6 > r+r1 > -1 and 6 > c+c1 > -1 and 6 > r-r1 > -1 and 6 > c-c1 > -1 and m[r+r1][c+c1] != "T" and m[r+r1][c+c1] != "t" and m[r+r1][c+c1] == "x" and m[r-r1][c-c1] == "O"]
                    # print("\nA ", around)
                    # print("A2 ", around2)

        if around2:
            shot = random.choice(around2)
        elif around:
            shot = random.choice(around)
        else:
            rand = []
            m = self.user_matrix.copy()
            for r, row in enumerate(self.user_matrix):
                for c, i in enumerate(row):
                    if i not in ['x', 'X', 't', 'T']:
                        rand.append([r, c])
            # print("random", end=" ")
            shot = random.choice(rand)

        rw = ""
        cw = ""
        for k, v in {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}.items():
            if v == shot[0]:
                rw = k
        for k, v in {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}.items():
            if v == shot[1]:
                cw = k
        print("shot in "+rw+cw)
        time.sleep(3)
        return shot

    def if_win(self):
        for row in self.user_matrix:
            for i in row:
                if i == "■":
                    return False
        return True


if __name__ == '__main__':
    sheeps = [3, 2, 2, 1, 1, 1, 1]
    g = Game()
    if input("1) Игра с ботом\n2) Игра с другом\nВведите 1 или 2: ") == 1:
        user1 = Persone(input("Введите ваше имя: "))
        user2 = Persone("Hello world!")
        user2.creat_sheep(sheeps=sheeps, test=True, rand=True)
        user1.creat_sheep(sheeps=sheeps)
    else:
        user1 = Persone(input("Введите имя ПЕРВОГО игрока: "))
        user1.creat_sheep(sheeps=sheeps)
        print("\n"*50)
        user2 = Persone(input("Введите имя ВТОРОГО игрока: "))
        user2.creat_sheep(sheeps=sheeps)
    for i in range(100):
        print('\n' * 40)
        print('\n════════════════════════════════')
        if i % 2 == 0:
            print(user1.user_name, "\n════════════════════════════════\n")
            user2.shoot(contr_user_name=user1.user_name)
        else:
            print(user2.user_name, "\n════════════════════════════════\n")
            user1.shoot(contr_user_name=user2.user_name)




