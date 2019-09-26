import numpy as np
import pandas as pd


class Team:
    """
        Class of a team
    """
    def __init__(self, name, players_df, strength):
        """
            Initialize object
        :param name: team number. Based on alphabetical order -> Arsenal = 1, ..., Wolves = 20
        :param players_df: DataFrame containing information about the players on the team
        :param strength: int providing information about how strong the team is.
        """
        self.name = name
        self.strength = strength
        self.players_df = players_df


class Players:
    """
        Class of FPL players.
    """
    def __init__(self, information_players):
        """
            Initialize object
        :param information_players: list of dictionaries with information about players
        """
        df = pd.DataFrame(information_players)
        float_columns = ['form', 'points_per_game', 'selected_by_percent']  # ensure float from strings
        df[float_columns] = df[float_columns].astype(float)
        length_news = df['news'].str.len()
        df.loc[:, 'fitness'] = length_news.values == 0  # create boolean for fitness/available players
        new_names = {'web_name': 'name', 'now_cost': 'price', 'selected_by_percent': 'selection',
                     'element_type': 'position'}  # new and better names for columns
        df = df.rename(columns=new_names)
        # decide attributes to keep
        attributes_to_use = ['name', 'price', 'team', 'total_points', 'points_per_game', 'minutes', 'form',
                             'clean_sheets', 'assists', 'goals_scored', 'selection', 'position', 'fitness']
        self.players_df = df[attributes_to_use]

    def get_attribute_from_all_players(self, attribute):
        if attribute not in self.players_df.keys():
            print(f'Attribute {attribute} does not exist for a player!')
            exit(1)
        return self.players_df[attribute]

    def create_all_teams(self):
        list_of_teams_df = [x for _, x in self.players_df.groupby('team')]
        team_list = []
        for i in range(len(list_of_teams_df)):
            team = Team(list_of_teams_df[i]['team'].values[0], list_of_teams_df[i], 10)
            team_list.append(team)
        return team_list


class Fixtures:
    # TODO: how to get fixture information?
    """
        Class of Fixtures
    """
    def __init__(self, fixture_information):
        self.gameweeks = range(1, 39)
        self.opponents = fixture_information['opponents']
        self.difficulty_ratings = fixture_information['difficulty_ratings']
        self.dates = fixture_information['dates']


class Squad:
    """
        Class of a selected squad with 15 players to be used in FPL
    """
    def __init__(self, players_df, fixture_information_player):
        """
            Initialize object
        :param players_df: DataFrame containing information about the players on the squad
        :param fixture_information_player: list of dictionaries with opponents, difficulty ratings and dates for each player
        """
        self.players_df = players_df
        self.fixtures = []
        for i in range(len(fixture_information_player)):
            self.fixtures.append(Fixtures(fixture_information_player[i]))
        self.max_price = 1000
        self.number_of_goalkeepers = 2
        self.number_of_defenders = 5
        self.number_of_midfielders = 5
        self.number_of_attackers = 3
        self.positions_sum = self.number_of_goalkeepers*1 + self.number_of_defenders*2 + \
                             self.number_of_midfielders*3 + self.number_of_attackers*4

    def validate_squad(self):
        prices = self.players_df['price'].values
        positions = self.players_df['position'].values
        total_cost_squad = np.sum(prices)
        below_check = total_cost_squad <= self.max_price
        sum_of_positions = np.sum(positions)
        position_check = sum_of_positions == self.positions_sum
        if below_check*position_check == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    test = 0
