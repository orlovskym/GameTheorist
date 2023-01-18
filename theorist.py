from console_interface import PyConsoleOutput


class Theorist:

    def __init__(self, game, interfaces=None):
        if interfaces is None:
            interfaces = [PyConsoleOutput()]
        self.my_game = game
        self.my_interfaces = interfaces
        self.math = {}
        self.refresh_game_math()
        self.output_game_info(name=self.my_game.name, description=self.my_game.description, players=self.my_game.players, strategies=self.my_game.strategies,
                              numbers=self.math)

    def refresh_game_math(self):
        """read updated numbers from my_game"""
        self.math["num_rows"] = self.my_game.get_number_rows()
        self.math["num_columns"] = self.my_game.get_number_columns()
        self.math["rows"] = []
        self.math["columns"] = []
        for i in range(self.math["num_rows"]):
            self.math["rows"].append(self.my_game.get_row(i))
        for i in range(self.math["num_columns"]):
            self.math["columns"].append(self.my_game.get_column(i))

    def output_game_info(self, name=False, description=False, players=False, strategies=False, numbers=None):
        """visualize my_game on all my_interfaces"""
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if players:
            data["players"] = players
        if strategies:
            data["strategies"] = strategies
        if numbers:
            data["numbers"] = numbers
        for interface in self.my_interfaces:
            interface.draw_data(data)

    def explain(self, string, newline=False):
        """output a string to all my interfaces"""
        for interface in self.my_interfaces:
            interface.output_thoughts(string)
            if newline:
                interface.newline()

    def get_best_response(self, player, opposing_strategy, verbose=True):
        """for player, return the index of the best response to enemy_strategy"""
        if player == 0:
            opponent = 1
            opponent_strategies = "columns"
        else:
            opponent = 0
            opponent_strategies = "rows"
        possibilities = self.math[opponent_strategies][opposing_strategy]
        possible_scores = []
        for i in range(len(possibilities)):
            possible_scores.append(possibilities[i][player])
        best_outcome = max(possible_scores)
        best_strategy = possible_scores.index(best_outcome)

        if verbose:
            player_name = self.my_game.players[player]
            opponent_name = self.my_game.players[opponent]
            player_strategy_names = self.my_game.strategies[player]
            opposing_strategy_name = self.my_game.strategies[opponent][opposing_strategy]
            best_strategy_name = self.my_game.strategies[player][best_strategy]
            options_string = []
            for i in range(len(possibilities)):
                options_string.append(f"I can {player_strategy_names[i]} and score {possible_scores[i]} points")
            options_string = ', or '.join(options_string)
            self.explain(f"If I know that {opponent_name} will {opposing_strategy_name}, "
                         f"{options_string}. The best option for me is to {best_strategy_name}.")

        return best_strategy

    def get_strictly_dominant_strategy(self, player, verbose=True):
        """returns the index of player's strictly best strategy"""
        best_strategies = []
        if verbose:
            player_name = self.my_game.players[player]
            print(f"Let's pretend I'm {player_name}.")
        if player == 0:
            opponent = 1
            opponent_strategies = "columns"
        else:
            opponent = 0
            opponent_strategies = "rows"

        for i in range(self.math[f"num_{opponent_strategies}"]):  # for every opponent strategy
            best_strategies.append(self.get_best_response(player, i, verbose))  # save my best response
        strictly_best_exists = (len(set(best_strategies)) == 1)

        if verbose:
            best_strategy_name = self.my_game.strategies[player][best_strategies[0]]
            opponent_name = self.my_game.players[opponent]
            if strictly_best_exists:
                self.explain(f"No matter what {opponent_name} does, my best option is to {best_strategy_name}.",
                             newline=True)
            else:
                self.explain(f"No one strategy is best regardless of what {opponent_name} chooses.", newline=True)

        if strictly_best_exists:
            return best_strategies[0]  # let me know what it is!
        else:
            return None

    def solve_by_strict_dominance(self, verbose=True):
        """each player checks for a strictly best strategy"""
        results = []
        for i in range(2):
            results.append(self.get_strictly_dominant_strategy(i, verbose))
        solved = (None not in results)

        if verbose:
            if solved:
                p1_name = self.my_game.players[0]
                p2_name = self.my_game.players[1]
                p1_strat = self.my_game.strategies[0][results[0]]
                p2_strat = self.my_game.strategies[1][results[1]]
                self.explain(f"{p1_name} should {p1_strat}, and {p2_name} should {p2_strat}.")
            else:
                self.explain("I can't solve this by checking for strict dominance.")

        if solved:
            return results
        else:
            return None

    def compare_strategies(self, index1, index2, player, verbose=True):
        """compare two player strategies, and remove the strictly worse one if it exists"""
        worse_strategy = []
        if player == 0:
            opponent = 1
            my_strategies = "rows"
            opponent_strategies = "columns"
        else:
            opponent = 0
            my_strategies = "columns"
            opponent_strategies = "rows"

        strategies = [self.math[my_strategies][index1], self.math[my_strategies][index2]]
        strategy_1 = strategies[0]
        strategy_2 = strategies[1]
        for i in range(self.math[f"num_{opponent_strategies}"]):  # for each of my strategies
            if strategy_1[i][player] > strategy_2[i][player]:  # compare two of my opponent's responses
                worse_strategy.append(index2)
            elif strategy_1[i][player] < strategy_2[i][player]:
                worse_strategy.append(index1)

        results = set(worse_strategy)
        found_worst = (len(results) == 1)  # notice if one of the two is always worse

        if verbose:
            my_name = self.my_game.players[player]
            if found_worst:
                better_strategy = [index1, index2]
                better_strategy.remove(worse_strategy[0])
                better_strategy_name = self.my_game.strategies[player][better_strategy[0]]
                worse_strategy_name = self.my_game.strategies[player][worse_strategy[0]]
                self.explain(
                    f"There is no situation in which {my_name} sees better results by choosing {worse_strategy_name} over {better_strategy_name}. We can eliminate {worse_strategy_name}.")
            # else:
            #     self.explain(
            #         "Both strategies have situations in which they are more effective; neither is obviously worse.")

        if found_worst:
            worse_strategy = worse_strategy[0]
            self.my_game.remove_strategy(worse_strategy, my_strategies)
            self.refresh_game_math()
            self.output_game_info(strategies=self.my_game.strategies, numbers=self.math)
            return True
        else:
            return None

    def check_for_strictly_dominated_strategy(self, player, verbose=True):
        should_stop = False

        if player == 0:
            my_strategies = "rows"
        else:
            my_strategies = "columns"

        index = self.math[f"num_{my_strategies}"]
        for i in range(index):  # for each of my strategies
            if should_stop:
                break
            for j in range(index):
                if i == j or j > i:
                    pass
                else:
                    should_stop = self.compare_strategies(i, j, player)
                    if should_stop:
                        break
        if should_stop:
            return True
        else:
            return None

    def solve_by_iterative_elimination(self):
        while True:
            results = []

            for i in range(2):
                results.append(self.check_for_strictly_dominated_strategy(i))

            if results == [None, None]:
                print("done")
                return

    def solve(self):
        pass