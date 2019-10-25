import numpy as np
import pandas as pd
import pickle


def team_number_to_name(team_number):
    number_to_name_dictionary = {1: 'Arsenal',
                                 2: 'Aston Villa',
                                 3: 'Bournemouth',
                                 4: 'Brighton & Hove Albion',
                                 5: 'Burnley',
                                 6: 'Chelsea',
                                 7: 'Crystal palace',
                                 8: 'Everton',
                                 9: 'Leicester City',
                                 10: 'Liverpool',
                                 11: 'Manchester City',
                                 12: 'Manchester United',
                                 13: 'Newcastle United',
                                 14: 'Norwich City',
                                 15: 'Sheffield United',
                                 16: 'Southampton',
                                 17: 'Tottenham Hotspur',
                                 18: 'Watford',
                                 19: 'West Ham',
                                 20: 'Wolverhampton Wanderers'}
    return number_to_name_dictionary[team_number]


def create_player_id_to_team(players):
    """
        Use Players object to create a dictionary for matching players ids with a team. Is going to be used
        to create data for machine learning
    :param players: Players object
    """
    ids = players.df['id']
    teams = players.df['team']
    dictionary = dict(zip(ids, teams))
    # Save dictionary as player_ids_to_team as a pickle
    with open('player_ids_to_team.pickle', 'wb') as handle:
        pickle.dump(dictionary, handle)


def create_player_id_to_position(players):
    ids = players.df['id']
    positions = players.df['position']
    dictionary = dict(zip(ids, positions))
    # Save dictionary as player_ids_to_team as a pickle
    with open('player_ids_to_position.pickle', 'wb') as handle:
        pickle.dump(dictionary, handle)


def get_position_from_player_id(player_id):
    # Load dictionary with player id -> position
    with open('player_ids_to_position.pickle', 'rb') as handle:
        player_ids_to_position_dict = pickle.load(handle)
    return player_ids_to_position_dict[player_id]


def get_gameweek_information(player_id, gameweek, fixtures):
    # Load dictionary with player id -> team
    with open('player_ids_to_team.pickle', 'rb') as handle:
        player_ids_to_team_dict = pickle.load(handle)
    team = player_ids_to_team_dict[player_id]
    team_fixtures = fixtures.list_teams[team-1]  # 0-indexed list
    gameweek_info = team_fixtures[team_fixtures['gameweek'] == gameweek]
    return gameweek_info


