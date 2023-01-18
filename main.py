from games_list import GAMES_LIST
from game import Game
from theorist import Theorist

pd = Game(GAMES_LIST["Prisoner's Dilemma"])
arms = Game(GAMES_LIST["Arms Race"])
pandc = Game(GAMES_LIST["Pacifist and Opportunist"])
duopoly = Game(GAMES_LIST["Duopoly"])

play = duopoly

solver = Theorist(game=play)
#solver.solve_by_strict_dominance()
#solver.compare_strategies(0, 1, 0)
solver.solve_by_iterative_elimination()













def dict_to_matrix(problem):
    """convert a dictionary to a 2d array"""
    x_cords = []
    y_cords = []
    for value in problem:
        x_cords.append(value[0])
        y_cords.append(value[1])
    rows = max(y_cords) + 1
    cols = max(x_cords) + 1
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for tile in problem:
        arr[tile[0]][tile[1]] = problem[tile]
    return arr



# def prompt(problem):
#     proceed = input("Would you like me to solve this game? Y or N: ").lower()
#     if proceed != 'y' and proceed != 'n':
#         prompt()
#     elif proceed == 'y':
#         problem.find_strictly_best_strategies()
#     else:
#         pass


# iesds = ProblemSolver(name="IESDS Demo",
#                       players=["Player 1", "Player 2"],
#                       strategies=[["Up", "Middle", "Down"],
#                                   ["Left", "Center", "Right"]],
#                       values=[[[13, 3], [1, 4], [7, 3]],
#                               [[4, 1], [3, 3], [6, 2]],
#                               [[-1, 9], [2, 8], [8, -1]]])
