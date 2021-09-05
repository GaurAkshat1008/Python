import math 
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):  
         pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. input numbers from (0-8)')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid Move')
    
        return val  

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        
        else:
            square = self.minimax(game, self.letter)['Position']
        return square
    def minimax(self, state, player):
        max_player = self.letter
        o_player = 'O' if self.letter == 'X' else 'X'
        if state.current_winner == o_player:
            return {'Position': None,  
            'Score': 1 * (state.num_empty_square() + 1) if o_player == max_player else -1 * (state.num_empty_square() + 1)
            }
        elif not state.empty_square():
            return {'Position': None, 'Score': 0}
        
        if player == max_player:
            best = {'Position': None, 'Score': -math.inf}
        else:
            best = {'Position': None, 'Score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, o_player)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['Position'] = possible_move


            if player == max_player:
                if sim_score['Score'] > best['Score']:
                    best = sim_score
            
            else:
                if sim_score['Score'] < best['Score']:
                    best = sim_score
        return best
