GAMES_LIST = {

    "Prisoner's Dilemma": {
        "name": "The Prisoner's Dilemma",
        "description": "Two prisoners have committed robbery together, but the prosecution can only prove "
                       "trespassing. Each prisoner can get a lighter sentence if they confess and implicate their "
                       "partner.",
        "players": ["Prisoner 1", "Prisoner 2"],
        "strategies": [["Keep Quiet", "Confess"],
                       ["Keep Quiet", "Confess"]],
        "values": [[[-1, -1], [-12, 0]],
                   [[0, -12], [-8, -8]]]},


    "Arms Race": {
        "name": "Arms Race",
        "description": "A new weapons technology has emerged that grants an armed state an advantage over a "
                       "state that is not similarly armed. Arming would be expensive, however.",
        "players": ["State 1", "State 2"],
        "strategies": [["Pass", "Build Weapons"],
                       ["Pass", "Build Weapons"]],
        "values": [[[3, 3], [1, 4]],
                   [[4, 1], [2, 2]]]},


    "Pacifist and Opportunist": {
        "name": "The Pacifist and the Opportunist",
        "description": "This is the same situation as Arms Race, except the Pacifist only cares about weapon "
                       "proliferation and loses a point for each state that arms.",
        "players": ["The Pacifist", "The Opportunist"],
        "strategies": [["Pass", "Build Weapons"],
                       ["Pass", "Build Weapons"]],
        "values": [[[0, 3], [-1, 4]],
                   [[-1, 1], [-2, 2]]]},


    "Duopoly": {
        "name": "Duopoly",
        "description": "Two firms can each produce a commodity for $1. The market price of the commodity is "
                       "$12-2*supply, so it will drop to $0 if at least 6 units are on the market.",
        "players": ["Firm 1", "Firm 2"],
        "strategies": [["Produce Zero", "Produce One", "Produce Two", "Produce Three", "Produce Four", "Produce Five"],
                       ["Produce Zero", "Produce One", "Produce Two", "Produce Three", "Produce Four", "Produce Five"]],
        "values": [[[0, 0], [0, 9], [0, 14], [0, 15], [0, 12], [0, 5]],
                   [[9, 0], [7, 7], [5, 10], [3, 9], [1, 4], [-1, -5]],
                   [[14, 0], [10, 5], [6, 6], [2, 3], [-2, -4], [-2, -5]],
                   [[15, 0], [9, 3], [3, 2], [-3, -3], [-3, -4], [-3, -5]],
                   [[12, 0], [4, 1], [-4, -2], [-4, -3], [-4, -4], [-4, -5]],
                   [[5, 0], [-5, -1], [-5, -2], [-5, -3], [-5, -4], [-5, -5]]]},

}
