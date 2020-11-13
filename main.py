def is_in_list(n, lst):
    for i in range(len(lst)):
        if lst[i] == n:
            return True
    return False

def intersection(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                result.append(lst2[j])
    return result

def is_valid_matrix(matrix):
    num_col = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) != num_col:
            return False
    return True


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def reverse(to_reverse):
    if len(to_reverse) < 2:
        return to_reverse
    return reverse(to_reverse[1:]) + to_reverse[0]

def print_list(lst):
    if not lst:
        return
    print lst[0]
    return print_list(lst[1:])

def is_in_list(n, lst):
    if not lst:
        return False
    else:
        return lst[0] == n or is_in_list(n, lst[1:])


def is_increasing(lst):
    if not lst: 
        return 
    if len(lst) < 2:
        return True
    if lst[0] > lst[1]:
        return False
    return is_increasing(lst[1:])

def filter_gt_n(lst, n):
    if not lst:
        return lst
    if lst[0] <= n:
        #print lst
        lst.remove(lst[0])
        return filter_gt_n(lst, n)
    return lst

def intersection(lst1, lst2):
    if not lst1:
        return []
    if lst1[0] in lst2 and len(lst1) > 0:
        return [lst1[0]] + intersection(lst1[1:], lst2)
    return intersection(lst1[1:], lst2)

def maze_solver(matrix, solution, pos_row, pos_col):

    len_col = len(matrix[0])
    len_row = len(matrix)

    # if we are on the winner spot
    if pos_row == len_row - 3 and pos_col == len_col - 1:
        return solution

    # If we go outboud
    if pos_row >= len_row or pos_col >= len_col:
        return None

    # If we hit a X spot
    if matrix[pos_row][pos_col] == "X":
        return None

    # We go right
    solution.append("r")
    sol_go_right = maze_solver(matrix, solution, pos_row, pos_col + 1)
    if sol_go_right is not None :
        return sol_go_right
    # We backtrack 
    solution.pop()

    #We go down
    solution.append("d")
    sol_go_down = maze_solver(matrix, solution, pos_row + 1 , pos_col)
    if sol_go_down is not None :
        return sol_go_down
    # We backtrack 
    solution.pop()

    return None


robot_maze = [
    ["E", "E", "E", "E" ],
    ["E", "X", "X", "E" ],
    ["E", "E", "E", "X" ],
    ["X", "X", "E", "X" ]
]

print maze_solver(robot_maze, [], 0, 0)

#[3, 4] 