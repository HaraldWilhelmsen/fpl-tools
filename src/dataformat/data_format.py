import numpy as np


class Player:
    """
        Class of FPL player
    """
    def __init__(self, player_information):
        """
            Initialize object
        :param player_information: dictionary containing information about player
        """
        self.name = player_information['web_name']
        self.price = int(player_information['now_cost'])
        self.team = int(player_information['team'])
        self.points = int(player_information['total_points'])
        self.average_points = float(player_information['points_per_game'])
        self.minutes_played = int(player_information['minutes'])
        self.form = float(player_information['form'])
        self.clean_sheets = int(player_information['clean_sheets'])
        self.assists = int(player_information['assists'])
        self.goals_scored = int(player_information['goals_scored'])
        self.selection = float(player_information['selected_by_percent'])
        if player_information['news'] != "":
            self.fitness = True
        else:
            self.fitness = False


class Fixtures:
    """
        Class of Fixtures
    """
    def __init__(self, fixture_information):
        self.gameweeks = range(1, 39)
        self.opponents = fixture_information['opponents']
        self.difficulty_ratings = fixture_information['difficulty_ratings']
        self.dates = fixture_information['dates']


class Team:
    """
        Class of a team
    """
    def __init__(self, name, player_information_team, fixture_information_team):
        """
            Initialize object
        :param name: name of team
        :param player_information_team: list of dictionaries with player information
        :param fixture_information_team: dictionary with opponents, difficulty ratings and dates
        """
        self.name = name
        self.players = []
        for i in range(len(player_information_team)):
            self.players.append(Player(player_information_team[i]))
        self.fixtures = Fixtures(fixture_information_team)


class Squad:
    """
        Class of a selected squad with 15 players to be used in FPL
    """
    def __init__(self, player_information_team, fixture_information_player):
        """
            Initialize object
        :param player_information_team: list of dictionaries with player information
        :param fixture_information_player: list of dictionaries with opponents, difficulty ratings and dates for each player
        """
        self.players = []
        self.fixtures = []
        for i in range(len(player_information_team)):
            self.players.append(Player(player_information_team[i]))
        for i in range(len(fixture_information_player)):
            self.fixtures.append(Fixtures(fixture_information_player[i]))
