from  random import shuffle

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
    
    MOVES = ['a', 'd', 'w', 's']
    
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
            
    def create_current_variant(self):
        random_moves = Game.MOVES * 50
        shuffle(random_moves)
        
        self.current_variant = self.goal_variant.copy()
        
        for i in random_moves:
            self.move(i)      
    
    

    def result_print(self):
        for x in self.current_variant:
            print('-' * 21)
            print(f'| {x[0].name} | {x[1].name} | {x[2].name} | {x[3].name} |')
            if x == self.current_variant[3]:
                print('-' * 21)

    def get_index_16(self):
        numb16 = 16
        for x in self.current_variant:
            for y in x:
                if y._numb == numb16:
                    return (self.current_variant.index(x), x.index(y))
        else:
            return (None,None)

    
    def move(self, key, comm = False):        
        x,y = self.get_index_16()
        comment_text = 'uncorrect move'
        if key == 'a':
            try:
                self.current_variant[x][y],self.current_variant[x][y-1] = self.current_variant[x][y-1], self.current_variant[x][y]
            except:
                if comm:
                    print(comment_text)
        elif key == 'd':
            try:
                self.current_variant[x][y],self.current_variant[x][y+1] = self.current_variant[x][y+1], self.current_variant[x][y]
            except IndexError:
                if comm:
                    print(comment_text)
                
        elif key == 'w':
            try:
                self.current_variant[x][y],self.current_variant[x-1][y] = self.current_variant[x-1][y], self.current_variant[x][y]
            except:
                if comm:
                    print(comment_text)
        elif key == 's':
            try:
                self.current_variant[x][y],self.current_variant[x+1][y] = self.current_variant[x+1][y], self.current_variant[x][y]
            except:
                if comm:
                    print(comment_text)
        else:
            if comm:
                    print(comment_text)
            
            
   

game = Game()

game.create_goal_variant()
game.create_current_variant()
game.result_print()


while not game.is_game_finished():
    key_m = input('a <, d >, w A, s V :')
    game.move(key_m, comm = True)
    game.result_print()

 
