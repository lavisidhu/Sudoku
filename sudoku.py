from pprint import pprint

def main():
    allowed_nums = {1,2,3,4,5,6,7,8,9}

    solution_space = [
        [ 8,    1, None,    7,    None,    None, None, 4,   9   ],
        [ 9,    None, 3, 6,    None, 2, None,    7, None ],
        [ None, 7,    None, None, 9,    None, 2, None, None    ],
        [ None, 5, None, None,    None, 7,    None, None,    6    ],
        [ None,    6, None,    None, 4, 5, 7,    None, None    ],
        [2,    None,    None, 1,    None, 9,    None, 3, None ],
        [ 5,    None, 1, None, None,    4, None, 6,    8 ],
        [ None, None, 8,    5, None, None,    None, 1, None   ],
        [ 7,    9,    None, 3, None,    None,    4,    None, None    ]
    ]

    is_solved = False
    while not is_solved:
        is_solved = True
        for i in range(0,9):     # row_index
            for j in range(0,9): # column_index
                if solution_space[i][j] == None:
                    allowed_values = allowed_nums \
                                     - row_set(i, solution_space) \
                                     - column_set(j, solution_space) \
                                     - ninth_set(i, j, solution_space)
                    if len(allowed_values) == 1:
                        x = list(allowed_values)
                        solution_space[i][j] = x[0]
                    else:
                        is_solved = False
    pprint(solution_space)

def row_set(row_index, solution_space):
    """
    Returns a set of numbers from solution_space row # row_index
    """
    row = set(solution_space[row_index])
    return row

def column_set(column_index, solution_space):
    """
    Returns a set of numbers from solution_space column # column_index
    """
    column_set = []

    for i in range(0,9):
        column_set.append(solution_space[i][column_index])

    return set(column_set)

def ninth_set(row_index, column_index, solution_space):
    """
    Returns a set of numbers from a ninth of solution_sapce
    where cell (row_index, column_index) is found
    """
    # Figure out which ninth we are in by x and y coordinate
    x = 3 * (row_index // 3)
    y = 3 * (column_index // 3)
    # (x,y) is the top corner of the ninth

    ninth_set = []
    for i in range(0,3):
        for j in range(0,3):
            ninth_set.append(solution_space[x+i][y+j])

    return set(ninth_set)

main()
