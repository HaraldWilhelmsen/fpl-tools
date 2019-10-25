from datafetch.fetch_data import DataFetch
from dataformat.classes import Players, Squad, Fixtures
import pandas as pd
import utility_functions as util_funcs


def create_team_list():
    a = DataFetch()
    b = a.get_current_fpl_info()
    player_info = b['elements']
    fixture_info = a.get_current_fixtures()

    players = Players(player_info, fixture_info)

    team_list = players.create_all_teams()  # list teams, where Arsenal = team_list[0], ... Wolves = team_list[-1]
    return team_list


def get_fixtures():
    a = DataFetch()
    fixture_info = a.get_current_fixtures()
    fixtures = Fixtures(fixture_info)
    return fixtures


def create_fpl_squad(list_of_player_names, list_of_player_teams):
    a = DataFetch()
    b = a.get_current_fpl_info()
    player_info = b['elements']
    fixture_info = a.get_current_fixtures()

    players = Players(player_info, fixture_info)
    squad_players = players.create_squad(list_of_player_names, list_of_player_teams)
    my_team = Squad(squad_players)
    return my_team


def choose_squad_based_on_attribute(choice_attribute):
    a = DataFetch()
    b = a.get_current_fpl_info()
    player_info = b['elements']
    fixture_info = a.get_current_fixtures()

    players = Players(player_info, fixture_info)
    df_all = players.df

    squad_df = pd.DataFrame()
    formation = [2, 5, 5, 3]
    for position in range(1, len(formation)+1):
        df = df_all.loc[df_all['position'] == position].copy()
        choices = df.sort_values(choice_attribute, ascending=False)
        squad_df = squad_df.append(choices[:formation[position-1]])
    print(squad_df)
    team = Squad(squad_df)  # create squad class. Is not a valid team since price is too high!


def get_gameweek_data(gameweek_number):
    a = DataFetch()
    b = a.get_gameweek_info(gameweek_number)
    gameweek_info = b['elements']
    gameweek_df = pd.DataFrame(gameweek_info)
    ids = gameweek_df['id']
    stats = gameweek_df['stats']
    df = pd.DataFrame(stats.to_list())
    float_columns = ['ict_index', 'influence', 'creativity', 'threat']
    df[float_columns] = df[float_columns].astype(float)
    df.loc[:, 'id'] = ids.values
    return df
