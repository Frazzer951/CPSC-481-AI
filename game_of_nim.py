from games import Game, GameState, alpha_beta_player, query_player


class GameOfNim(Game):
    def __init__(self, board=[0, 5, 3, 1]):
        moves = [(i, y) for i, x in enumerate(board) for y in range(1, x + 1)]
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=moves)

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        board = state.board.copy()
        board[move[0]] -= move[1]
        moves = [(i, y) for i, x in enumerate(board) for y in range(1, x + 1)]
        return GameState(
            to_move=("MIN" if state.to_move == "MAX" else "MAX"),
            utility=self.compute_utility(board, state.to_move),
            board=board,
            moves=moves,
        )

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        return state.moves

    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0 or len(state.moves) == 0

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == "MAX" else -state.utility

    def compute_utility(self, board, player):
        """If 'MAX' wins with this move, return 1; if 'MIN' wins return -1; else return 0."""
        if all(val == 0 for val in board):
            return +1 if player == "MAX" else -1
        else:
            return 0

    # def play_game(self, *players):
    #     """Play an n-person, move-alternating game."""
    #     state = self.initial
    #     while True:
    #         for player in players:
    #             print(f"\nInitial board: {state.board}")
    #             move = player(self, state)
    #             print(f"Player: {state.to_move} Move: {move}")
    #             state = self.result(state, move)
    #             print(f"New board: {state.board}")
    #             if self.terminal_test(state):
    #                 self.display(state)
    #                 return self.utility(state, self.to_move(self.initial))


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
