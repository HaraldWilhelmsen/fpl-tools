from datafetch.fetch_data import DataFetch
from dataformat.classes import Players


def create_team_list():
    a = DataFetch()
    b = a.get_current_fpl_info()
    player_info = b['elements']
    fixture_info = a.get_current_fixtures()

    players = Players(player_info, fixture_info)

    team_list = players.create_all_teams()  # list teams, where Arsenal = team_list[0], ... Wolves = team_list[-1]
    return team_list
