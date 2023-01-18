class Game:
    def __init__(self, game_data):
        self.name = game_data["name"]
        self.description = game_data["description"]
        self.players = game_data["players"]
        self.strategies = game_data["strategies"]
        self.matrix = game_data["values"]

    def get_number_rows(self):
        return len(self.matrix)

    def get_row(self, index):
        return self.matrix[index]

    def get_number_columns(self):
        return len(self.matrix[0])

    def get_column(self, index):
        column = []
        for i in range(self.get_number_rows()):
            column.append(self.matrix[i][index])
        return column

    def remove_column(self, index):
        new_matrix = []
        for row in range(self.get_number_rows()):  # for every row
            new_matrix.append([])  # add a row to the new matrix
            for column in range(self.get_number_columns()):  # for every column
                if column == index:
                    pass  # except the column that matches the provided index
                else:
                    new_matrix[row].append(self.matrix[row][column])  # copy the old matrix
        self.matrix = new_matrix  # then overwrite the old matrix
        del self.strategies[1][index]  # and delete the corresponding strategy name

    def remove_row(self, index):
        new_matrix = []
        for row in range(self.get_number_rows()):
            if row == index:
                pass
            else:
                new_matrix.append(self.matrix[row])
        self.matrix = new_matrix
        del self.strategies[0][index]

    def remove_strategy(self, index, which):
        if which == "rows":
            self.remove_row(index)
        elif which == "columns":
            self.remove_column(index)

    def is_last_strategy(self):
        if self.get_number_rows() == 1 or self.get_number_columns() == 1:
            return True
        else:
            return None
