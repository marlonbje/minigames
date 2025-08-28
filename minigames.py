import pandas as pd
import numpy as np

class MiniGame():
    def __init__(self):
        self.current_player = 0
        self.player1_annot = 'x'
        self.player2_annot = 'o'
        self.spaces = '.'
        self.playingfield = self.layout()
        
    def layout(self):
        while True:
            layout = input('TicTacToe or Four Connect? (1/2) ').strip()
            if layout == '1':
                self.game = 'TicTacToe'
                frame = np.array([self.spaces]*9).reshape(3,3)
                playingfield = pd.DataFrame(frame,columns=['1','2','3'],index=['A','B','C'])
                return playingfield
            elif layout == '2':
                self.game = 'Four Connect'
                frame = np.array([self.spaces]*25).reshape(5,5)
                playingfield = pd.DataFrame(frame,columns=['A','B','C','D','E'],index=[0,1,2,3,4])
                return playingfield
            else:
                print('invalid input\n')

    def get_player(self):
        if self.current_player == 0:
            self.current_player += 1
            return self.player1_annot
        else:
            self.current_player -= 1
            return self.player2_annot

    def move(self,playingfield,field):
        if self.game == 'Four Connect':
            self.field = field[0].upper()
            if self.field in self.playingfield.columns:
                if self.spaces in self.playingfield[self.field].values:
                    for i in range(5):
                        if self.playingfield.loc[i,self.field] == self.spaces:
                            last_free_index = i
                    self.playingfield.loc[last_free_index,self.field] = self.get_player()
                    print(f'\n{self.playingfield}')
                else:
                    print('column full')
            else:
                print('no such column')
        else:
            try:
                row = field[0].upper()
                column = field[1]
                if column in self.playingfield.columns and row in self.playingfield.index:
                    if self.playingfield.loc[row,column] == self.spaces:
                        self.playingfield.loc[row,column] = self.get_player()
                        print(f'\n{self.playingfield}')
                    else:
                        print('field already occupied')
                else:
                    print('no such field')
            except IndexError:
                print('incomplete input')

    def configure(self):
        while True:
            config = input('\nconfig player figures? (y/n) ').lower().strip()
            if config == 'y':
                self.player1_annot = input('\nplayer1 figure? ').strip()
                self.player2_annot = input('player2 figure? ').strip()
                break
            elif config == 'n':
                break
            else:
                print('invalid input')
                
    def play(self):
        self.configure()
        print(f'\n{self.playingfield}')
        while self.spaces in self.playingfield.values:
            if self.current_player == 0:
                self.move(self.playingfield,input(f'\nplayer {self.player1_annot}: field? ').strip())
            else:
                self.move(self.playingfield,input(f'\nplayer {self.player2_annot}: field? ').strip())

if __name__ == '__main__':
    Game = MiniGame()
    Game.play()