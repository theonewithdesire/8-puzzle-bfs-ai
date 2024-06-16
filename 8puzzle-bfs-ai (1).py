# 8 puzzle
# 0 is presented as blank
# matrix is the initial state
matrix = [[1, 4, 2],
          [3, 0, 8],
          [6, 5, 7]]


# function that moves zero (blank) to the right if possible
def moveRight(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if j < len(matrix[i]) - 1:  # check it there's further right to zero
                    matrix[i][j], matrix[i][j+1] = matrix[i][j +
                                                             1], matrix[i][j]  # swap blank to right
                    show(matrix)
                    return

# function that moves zero (blank) to the left if possible


def moveLeft(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if j - 1 >= 0:  # check if there's further left to zero
                    matrix[i][j], matrix[i][j-1] = matrix[i][j -
                                                             1], matrix[i][j]  # swap blank to left
                    show(matrix)
                    return

# function that moves zero (blank) to the up if possible


def moveUp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i - 1 >= 0:  # check if there's further up to zero
                    matrix[i][j], matrix[i-1][j] = matrix[i -
                                                          1][j], matrix[i][j]  # swap blank to up
                    show(matrix)
                    return

# function that moves zero to the down if possible


def moveDown(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i + 1 < len(matrix):  # check if there's further down to zero
                    matrix[i][j], matrix[i+1][j] = matrix[i +
                                                          1][j], matrix[i][j]  # swap  blank to down
                    show(matrix)
                    return

# function that shows the 8-puzzle state


def show(matrix):
    for row in matrix:
        print(row)
    print('----------')


goal_state = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]


def is_goal_state(matrix):
    return matrix == goal_state


def bfs_solver(initial_state):
    # using queue structure for breath first search algorithm
    queue = [(initial_state, [])]

    while queue:
        current_state, path = queue.pop(0)
        if is_goal_state(current_state):
            print("Goal state reached!")
            print("Solution path:")
            for step in path:  # generating the solution
                show(step)
            return

        # Generate and explore valid neighbor states
        # generating the neighbors using the defined functions
        for move_func in [moveLeft, moveUp, moveRight, moveDown]:
            new_state = [row[:] for row in current_state]
            move_func(new_state)
            queue.append((new_state, path + [new_state]))

    print("No solution found!")


bfs_solver(matrix)

# the summary of code
# 1 : makking the 8 puzzle layout using nested list
# 2 : making moving functions in order to change the states and later on to be used to generating valid neighbors to the current node
# 3 : laying out bfs algorithm using quque without any visited list in order to check the already visited nodes again if necessary
