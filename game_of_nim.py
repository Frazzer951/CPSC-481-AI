from games import Game, alpha_beta_player, query_player, GameState


class GameOfNim(Game):
    def __init__(self, board=[0, 5, 3, 1]):
        moves = [(i, y) for i, x in enumerate(board) for y in range(1, x + 1)]
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=moves)

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move[0]] -= move[1]
        moves = [(i, y) for i, x in enumerate(board) for y in range(1, x + 1)]
        return GameState(
            to_move=("MIN" if state.to_move == "MAX" else "MAX"),
            utility=0,
            board=board,
            moves=moves,
        )

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        return state.moves

    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        for val in state.board:
            if val != 0:
                return False
        return True

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if self.terminal_test(state):
            return +1 if player == "MAX" else -1
        raise NotImplementedError


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board)  # must be [0, 5, 3, 1]
    print(nim.initial.moves)  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 3)))

    print("\n\nGame Start")
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
