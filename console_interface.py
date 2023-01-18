from tabulate import tabulate
from textwrap import TextWrapper


class PyConsoleOutput:

    def __init__(self):
        self.wrapper = TextWrapper(width=100)

    def draw_data(self, data):
        keys = data.keys()
        if "name" in keys:
            print(f"\nThis game is called {data['name']}.")
        if "description" in keys:
            self.output_thoughts(data["description"])
        if "players" in keys:
            print(f"{data['players'][0]} is playing against {data['players'][1]}.")
        if "numbers" not in keys:

            if "strategies" in keys:
                if data["strategies"][0] == data["strategies"][1]:
                    print(f"Both players can choose between {' or '.join(data['strategies'][0])}.\n")
                else:
                    print(f"Possible moves are {data['strategies'][0]} against {data['strategies'][1]}.\n")
            return

        table = []
        header = []
        for row in range(data["numbers"]["num_rows"]):  # for every row
            table.append([])  # create a row in the display table
            if "strategies" in keys:  # if strategy names were provided
                table[row].append(data["strategies"][0][row])  # populate [0] of each row with a p1 strategy name
            for column in range(data["numbers"]["num_columns"]):
                table[row].append(data["numbers"]["rows"][row][column])  # add the appropriate numbers
                if "strategies" in keys:
                    if row == 0:  # and the first time
                        header.append(data["strategies"][1][column])  # add the name of the p2 strategy to the header

        print(f"\n{tabulate(table, headers=header)}\n")

    def output_thoughts(self, string):
        output = self.wrapper.wrap(text=string)
        for line in output:
            print(line)

    def newline(self):
        print()