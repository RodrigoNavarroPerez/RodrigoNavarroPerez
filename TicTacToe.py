import math
import numpy as np

class TicTacToe:
    def ___init___(self):
        self.row_count = 7
        self.column_count = 6
        self.action_size = self.column_count      #hecho

    def get_initial_state(self):
        return np.zeros ((self.row_count,self.column_count))


    def get_next_state(self,state,action,player):
        row = action // self.row_count
        column = action % self.column_count
        state[row,column] = player
        return state

    def check_win(self,state,action):
           for row in state:
        for i in range(len(row) - 3):
            if row[1] == row[i + 1] == row[i + 2] == row[i + 3] != 0:
                return row[i]

    for col in range(len(state[0])):
        for i in range(len(state - 3))
            if state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][col] != 0:
              return state[i][col]

    for i in range(len(state) - 3):
        for j in range(len(state[0]) - 3):
            if state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3]!= 0:
               return state[i][j]

    for i in range(len(state) - 3):
        for j in range(3, len(state[0])):
            if state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3]!= 0:
               return state[i][j]
    
    if np.all(state != 0):
        print("No hay jugadas")
        return 3

    return 0

    def get_value_and_terminated(self,state,action):
        if self.check_win(state,action):
            return 1,True
        if np.sum(self.get_valid_moves(state)) == 0:
            return 0, False

        return 0, False

    def get_opponent(self, player):
        return -player


    def get_valid_moves(self,state):
        return (state.reshape(-1)==0).astype(np.unit8)

    def get_opponent(self, player):
        return -player

    def change_perspective(self,state,player):
        return state*player

if __name__ == '__main__':
    tablero=TicTacToe()
    player = 1
    state = tictactoe.get_initial_state()

    args = {
        'C': 2,
        'num_searches':2000

    }

    mcts = MCTS(tresraya, args)

    state = tictactoe.get_initial_state()

while True:
    print(state)

    if player == 1:
        valid_moves = tresraya.get_valid_moves(state)
        print("Valid moves", [i for i in range(tresraya.action_size) if valid_moves[i] == 1])
        action = int(input(f"{player}: "))

        if valid_moves[action] == 0:
            print("action not valid")
            continue
    else:
        natural_state = tresraya.change_perspective(state,player)
        mcts_probs = mcts.search(neutral_state)
        print(mcts_probs)
        action = np.argmax(mcts_probs)

    state= tictactoe.get_next_state(state, action, player)
     
    value, is_terminal = tictactoe.get_value_and_terminated(state,action)

    if is_terminal:
        print(state)
        if value ==1:
            print("Player",player,"won.")
        else:
            print("Draw")
        break
    
    player =tresraya.get_opponent(player)

                    