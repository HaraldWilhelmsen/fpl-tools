from datafetch.fetch_data import DataFetch
from dataformat.classes import Players

import matplotlib.pyplot as plt

master_flag = {
            -1: 'test space',
        }[-1]

if __name__ == '__main__':
    if master_flag == 'test space':
        a = DataFetch()
        b = a.get_saved_fpl_info()
        player_info = b['elements']
        selected_players_info = player_info[:]
        players = Players(selected_players_info)
        prices = players.get_attribute_from_all_players('price').values
        points = players.get_attribute_from_all_players('total_points').values
        df = players.players_df
        print(df.head())
        # print(df)
        print(df.sort_values('selection', ascending=False).head())
        team_list = players.create_all_teams()
        Arsenal = team_list[0]
        print(Arsenal.players_df.sort_values('total_points', ascending=False).head())
