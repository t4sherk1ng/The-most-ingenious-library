import time
from datetime import datetime


class Button:
    def __init__(self):
        self.count = 0


    def click(self):
        self.count += 1


    def click_count(self):
        return self.count


class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0


    def add_left(self, left):
        self.left += left


    def add_right(self, right):
        self.right += right


    def result(self):
        if self.left > self.right:
            return 'L'
        elif self.left < self.right:
            return 'R'
        else:
            return '='


class OddEvenSeparator:
    def __init__(self):
        self.even_numbers = []
        self.odd_numbers = []


    def add_number(self, number):
        if number % 2:
            self.odd_numbers.append(number)
        else:
            self.even_numbers.append(number)


    def even(self):
        return self.even_numbers


    def odd(self):
        return self.odd_numbers


class LittleBell:
    def __init__(self):
        self.ding = 'ding'


    def sound(self):
        print(self.ding)


class BigBell:
    def __init__(self):
        self.n = 0


    def sound(self):
        print('dong' if self.n % 2 else 'ding')
        self.n += 1


class MinMaxWordFinder:
    def __init__(self):
        self.words = {}


    def add_sentence(self, sentence):
        self.words.update({i: len(i) for i in sentence.split(' ')})


    def shortest_word(self):
        m = min(self.words.values())
        x = []
        for i in self.words.keys():
            if self.words[i] == m:
                x.append(i)
        return  x


    def longest_word(self):
        m = max(self.words.values())
        x = []
        for i in self.words.keys():
            if self.words[i] == m:
                x.append(i)
        return  x


class Paragraph:
    def __init__(self, width):
        self.words = []
        self.width = width


    def add_word(self, word):
        self.words.append(word)


    def words(self):
        print(self.words)


class LeftParagraph(Paragraph):
    def end(self):
        result = ''
        length = 0
        for word in self.wordsList:
            if length+len(word) <= self.width:
                result += word
                length += len(word)
            else:
                result += '\n' + word
                length = len(word)
            if length+1 < self.width:
                result += ' '
                length += 1
        print(result)



class Stat:
    def __init__(self):
        self.numbers = []


    def add_number(self, n):
        self.numbers.append(n)


class MinStat(Stat):
    def result(self):
        return min(self.numbers)


class MaxStat(Stat):
    def result(self):
        return max(self.numbers)


class AverageStat(Stat):
    def result(self):
        s = sum(self.numbers)
        l = len(self.numbers)
        return s/l


class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates


    def get_proteins(self):
        return self.proteins


    def get_fats(self):
        return self.fats


    def get_carbohydrates(self):
        return self.carbohydrates


    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates


    def __add__(self, object):
        return FoodInfo(self.proteins + object.get_proteins(), self.fats + object.get_fats(), self.carbohydrates + object.get_carbohydrates())


class ReversedList:
    def __init__(self, lst):
        lst.reverse()
        self.lst = lst


    def __getitem__(self, item):
        return self.lst[item]


    def __len__(self):
        return len(self.lst)


class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


class Date:
    def __init__(self, month, day):
        d = datetime.strptime(".".join([str(day), str(month), '2005']), "%d.%m.%Y")
        self.time = time.mktime(d.timetuple())


    def get_time(self):
        return self.time


    def __sub__(self, other):
        return int((self.time - other.get_time()) / 86400)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def __eq__(self, other):
        return self.x == other.get_x() and self.y == other.get_y()


    def __ne__(self, other):
        return not self.__eq__(other)


class SparseArray:
    def __init__(self):
        self.n = [0 for i in range(0, 10)]


    def __getitem__(self, item):
        return self.n[item]


    def __setitem__(self, key, value):
        self.n[key] = value


class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def get_coordinates(self):
        return self.x, self.y, self.z


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass


class User:
    def __init__(self, id):
        self.id = id


    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):
     def check_solution(self, user, n):
         pass


class Admin(User):
     def edit(self,n):
         pass


class SuperAdmin(User):
    def grant(self, user):
        pass


class Summator:
    def __init__(self):
        pass

    def transform(self, n):
        return n

    def sum(self, n):
        res = 0
        for i in range(0, n + 1):
            res += self.transform(i)
        return res


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


# Инициализация цвета
color = WHITE
# Проверка цвета
##if color == BLACK:
  ##  do_something()
# сравнение цветов
##color == other_color
# Цвет противника
opponent_color = opponent(color)


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        # Пешка белого цвета в клетке E2.
        for i in range(0, 8):
            self.field[1][i] = Pawn(1, i, WHITE)
            self.field[6][i] = Pawn(6, i, BLACK)
        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)
        self.field[7][7] = Rook(7, 7, BLACK)
        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)
        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)
        self.field[0][2] = Elephant(0, 2, WHITE)
        self.field[0][5] = Elephant(0, 5, WHITE)
        self.field[7][2] = Elephant(7, 2, BLACK)
        self.field[7][5] = Elephant(7, 5, BLACK)
        self.field[0][3] = Queen(0, 3, WHITE)
        self.field[7][3] = Queen(7, 3, BLACK)
        self.field[0][4] = King(0, 4, WHITE)
        self.field[7][4] = King(7, 4, BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.field[row1][col1] != None:
            return False
        self.field[row][col] = None
        if char == "P":
            self.field[row1][col1] = Pawn(row1, col1, self.color)
        elif char == "R":
            self.field[row1][col1] = Rook(row1, col1, self.color)
        elif char == "K":
            self.field[row1][col1] = Knight(row1, col1, self.color)
        elif char == "Q":
            self.field[row1][col1] = Queen(row1, col1, self.color)
        elif char == "E":
            self.field[row1][col1] = Elephant(row1, col1, self.color)
        self.color = opponent(self.color)
        return True

    def move(self, row, col, row1, col1):
        if row == row1:
            if col1 - col > 0:
                for i in range(col + 1, col1):
                    if self.field[row][i]:
                        return False
                return True
            else:
                for i in range(col1 + 1, col):
                    if self.field[row][i]:
                        return False
                return True


        elif col == col1:
            if row1 - row > 0:
                for i in range(row + 1, row1):
                    if self.field[i][col]:
                         return False
                return True
            else:
                 for i in range(row1 + 1, row):
                        if self.field[i][col]:
                              return False
                 return True
        elif row - row1 == col - col1:
            if col1 - col > 0:
                for i in range(1, col1 - col):
                     if self.field[row + i][col + i]:
                      return False
                return True
            else:
                 for i in range(1, col - col1):
                    if self.field[row - i][col - i]:
                        return False
                 return True

        else:
            if col1 - col > 0:
                 for i in range(1, col1 - col):
                    if self.field[row - i][col + i]:
                        return False
                 return True
            else:
                 for i in range(1, col - col1):
                     if self.field[row + i][col - i]:
                         return False
                 return True


    def castling0(self):
        color_row = 0 if self.color == WHITE else 7

        if self.cell(color_row, 0)[1] != 'R' or self.cell(color_row, 4)[1] != 'K' or self.field(color_row, 0).is_change() or self.field(color_row, 4).is_change() or self.field(color_row, 1) != None or self.field(color_row, 2) != None:
            return False
        self.field(color_row, 1) = King(color_row, 1, self.color)
        self.field(color_row, 2) = Rook(color_row, 2, self.color)
        self.field(color_row, 0) = None
        self.field(color_row, 4) = None
        return True


    def castling7(self):
        color_row = 7 if self.color == BLACK else 0

        if self.cell(color_row, 0)[1] != 'R' or self.cell(color_row, 4)[1] != 'K' or self.field(color_row, 0).is_change() or self.field(color_row, 4).is_change() or self.field(color_row, 1) != None or self.field(color_row, 2) != None:
            return False
        self.field(color_row, 1) = King(color_row, 1, self.color)
        self.field(color_row, 2) = Rook(color_row, 2, self.color)
        self.field(color_row, 0) = None
        self.field(color_row, 4) = None
        return True


    def is_under_attack(self, row, col, color):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.field(i, j) != None and self.field(i, j).get_color() == color and self.field(i, j).can_move(row, col) and self.move(i, j, row, col):
                    return True
        return False




class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.moved = 0

    def set_position(self, row, col):
        self.row = row
        self.col = col
        self.moved = 1

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False

        return True


    def is_change(self):
        return self.moved()

class Knight:


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    def set_position(self, row, col):
        self.row = row
        self.col = col


    def char(self):
            return 'N'


    def get_color(self):
        return self.color


    def can_move(self, row, col):
        if abs(row - self.row) == 3 and abs(col - self.col) == 1 or abs(row - self.row) == 1 and abs(col - self.col) == 3:
            return True
        return False



class Queen:


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    def set_position(self, row, col):
        self.row = row
        self.col = col


    def char(self):
            return 'Q'


    def get_color(self):
        return self.color


    def can_move(self, row, col):
        if self.row != row and self.col != col or abs(row - self.row) == abs(col - self.col):
            return True
        return False


class Elephant:



    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    def set_position(self, row, col):
        self.row = row
        self.col = col


    def char(self):
            return 'E'


    def get_color(self):
        return self.color


    def can_move(self, row, col):
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False


class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.moved = 0


    def set_position(self, row, col):
        self.row = row
        self.col = col
        self.moved = 1


    def char(self):
            return 'K'


    def get_color(self):
        return self.color


    def can_move(self, row, col):
        if abs(row - self.row) == 1 and abs(col - self.col) == 1:
            return True
        return False


    def get_change(self):
        return self.is_change


    def is_change(self):
        return self.moved()


class Server:
    def __init__(self):
        self.userlist = []
        self.maillist = {}


    def registration(self, user):
        self.userlist.append(user)


    def authorization(self, user):
        return user in self.userlist


    def add_mail(self, getter, sender, message):
        self.maillist[getter].append({'sender': sender, 'message': message})


    def get_user_mail(self, user):
        return self.maillist[user]


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user


    def receive_mail(self):
        return self.server.get_user_mail(self.user)


    def send_mail(self, server, user, message):
        server.add_mail(user, self.user, message)
        return True


class Numbers:
    def __init__(self):
        self.list = {}
