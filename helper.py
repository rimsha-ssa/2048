import random

def new_game(n):
    """
    Create an empty nxn matrix (2 dimensional list)
    returns:
        4x4 matrix with 0 in all cells
    """
    matrix = []

    for _ in range(n):
        matrix.append([0] * n)
    return matrix


def add_two(mat):
    """
    Randomly places the digit 2 in the remaining empty cells of matrix
    returns:
        Updated matrix
    """
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while(mat[a][b] != 0):
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat


def game_state(mat):
    """
    Keeping track of game state with each move
    returns:
        Game state: win/lose/continued
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat)-1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'continued'
    for i in range(len(mat)):  # check for any zero entries
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'continued'
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'continued'
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'continued'
    return 'lose'


def reverse(mat):
    """
    Helper function to flip rows for summing (merge) when right key is pressed
    Returns:
        2D list - Updated matrix
    """
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def transpose(mat):
    """
    Helper function to transpose rows for summing (merge) when up/down event is called
    Returns:
        2D list - Updated matrix
    """
    new = []
    for row in range(len(mat[0])):
        new.append([])
        for column in range(len(mat)):
            new[row].append(mat[column][row])
    return new


def cover_up(mat):
    """
    Update position of merged cells
    Returns:
        2D list - Updated matrix
        done - boolean
    """
    new = [
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]
          ]
    done = False
    for row in range(4):
        count = 0
        for column in range(4):
            if mat[row][column] != 0:
                new[row][count] = mat[row][column]
                if column != count:
                    done = True
                count += 1
    return (new, done)


def merge_values(mat):
    """
    Sum the values of each column/row on any arrow key event 
    when the corresponding next value is same
    Returns:
        2D list - Updated matrix
        done - boolean to tell whether any merge happened
    """
    done = False
    for row in range(4):
        for column in range(3):
            if mat[row][column] == mat[row][column+1] and mat[row][column] != 0:
                mat[row][column] *= 2
                mat[row][column+1] = 0
                done = True
    return (mat, done)


def up(game):
    """
    Up key event
    """
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge_values(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return (game, done)


def down(game):
    """
    Down key event
    """
    game = reverse(transpose(game))
    game, done = cover_up(game)
    temp = merge_values(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return (game, done)


def left(game):
    """
    Left key event
    """
    # return matrix after shifting left
    game, done = cover_up(game)
    temp = merge_values(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return (game, done)


def right(game):
    """
    Right key event
    """
    # return matrix after shifting right
    game = reverse(game)
    game, done = cover_up(game)
    temp = merge_values(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = reverse(game)
    return (game, done)
