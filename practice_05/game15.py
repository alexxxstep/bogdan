
n = 1
n_list = []

class Number:
    def __init__(self):
        self._numb = 0
        self.name = ''

    @property
    def numb(self):
        return self._numb

    @numb.setter
    def numb(self, numb_val):
        numbers = [i for i in range(1, 17)]
        if numb_val in numbers:
            self._numb = numb_val
            if numb_val <10:
                self.name = f'{numb_val} '
            elif numb_val == 16:
                self.name = '  '
            else:
                self.name = f'{numb_val}'


class Game:
    def __init__(self):
        self.goal_variant = []
        self.current_variant = []

    def is_game_finished(self):
        return self.goal_variant == self.current_variant

    def create_goal_variant(self):
        n = 1
        while n < 16:
            n_iner = []
            for y in range(4):
                number_f = Number()
                number_f.numb = n
                n_iner.append(number_f)
                n += 1
            self.goal_variant.append(n_iner)

    def result_print(self):
        for x in self.goal_variant:
            print('-' * 21)
            print(f'| {x[0].name} | {x[1].name} | {x[2].name} | {x[3].name} |')
            if x == self.goal_variant[3]:
                print('-' * 21)

    def get_index_16(self):
        num = 16
        for x in self.goal_variant:
            for y in self.goal_variant.x:
                pass




    def move_right(x, y):
        pass

    def move_left(x, y):
        pass

    def move_up(x, y):
        pass

    def move_down(x, y):
        pass


game = Game()

game.create_goal_variant()
game.result_print()

game.move_left()

