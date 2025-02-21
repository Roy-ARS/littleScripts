def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    if 0 <= to_row < len(game_matrix) and 0 <= to_column < len(game_matrix):
        if from_row == to_row:
            if (from_column - to_column == 1) or (to_column - from_column in range(1,3) and game_matrix[to_row][to_column-1]):
                return game_matrix[to_row][to_column]
        elif from_column == to_column:
            if (from_row - to_row == 1) or (to_row - from_row == 1):
                return game_matrix[to_row][to_column]
    return False

if __name__ == "__main__":
    gameMatrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(gameMatrix, 3, 2, 2, 2)) # True, Valid move
    print(can_travel_to(gameMatrix, 3, 2, 3, 4)) # False, Can't travel through land
    print(can_travel_to(gameMatrix, 3, 2, 6, 2)) # False, Out of bounds