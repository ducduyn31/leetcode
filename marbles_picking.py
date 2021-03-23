from typing import List


def take_marbles(current_marbles: int, is_X_turn: bool, available_moves: List[int]) -> int:
    """
    Simulate "marble steal" game using minimax (recursive) algorithm.
    There will be 2 players: X and Y. They are allowed to pick a
    number of marbles on table. The game finishes when there is only
    1 marble left.

    Example:
    Initially, there are 6 marbles on the board.
    One of the players can choose to remove 1 or 2 marbles leaving 5 or 4,
    after that the other player can do the same, choosing to take again one
    or two marbles from the board. The process continue until there is
    only one marble in the board. The player who wins is the one the
    leaves the last marble on the board.

    :param current_marbles: how many marbles are there to pick
    :param is_X_turn: whom turn is it
    :param available_moves: how many marbles player is allowed to pick
    :return: 1 means X win, -1 means Y win
    """

    # The game finish when there is only 1 player left
    if current_marbles == 1:
        # if it is X turn then the previous player ( player Y )
        # who leaves 1 marble is the winner
        return -1 if is_X_turn else 1

    # calculate next available moves so there will be at
    # least 1 marble on the table
    next_move = list(filter(lambda x: current_marbles - x >= 1, available_moves))

    if is_X_turn:
        # X will try to maximize his chance of winning by
        # taking the higher score between taking 1 marble
        # of 2 marbles from the table
        return max([take_marbles(current_marbles - move, False, next_move) for move in next_move])
    else:
        # Y will try to maximize his chance of winning
        # by taking the lower score (lower chance
        # for X to win) between taking 1 marble of
        # 2 marbles from the table
        return min([take_marbles(current_marbles - move, True, next_move) for move in next_move])


if __name__ == '__main__':
    # Result in 1, means X will win if both X and Y
    # both try to maximize their winning rate
    print(take_marbles(6, True, [1, 2]))
