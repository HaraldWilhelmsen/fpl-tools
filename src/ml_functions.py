import numpy as np
import pandas as pd

import fpl_functions as fpl_funcs
import utility_functions as util_funcs


def get_all_gameweeks(latest_gameweek):
    list_of_gameweek_dfs = []
    for i in range(1, latest_gameweek+1):
        list_of_gameweek_dfs.append(fpl_funcs.get_gameweek_data(i))
    return list_of_gameweek_dfs


def update_gameweek_with_position_and_fixture_information(gw_dfs, fixtures):
    for i in range(len(gw_dfs)):
        gw = gw_dfs[i]
        gw.loc[:, 'position'] = 0
        gw.loc[:, 'opponent_difficulty'] = 0
        gw.loc[:, 'H/A'] = 0
        ids = gw['id'].values
        for id in ids:
            position = util_funcs.get_position_from_player_id(id)
            gw.loc[gw['id'] == id, 'position'] = position
            fixture = util_funcs.get_gameweek_information(id, i+1, fixtures)
            gw.loc[gw['id'] == id, 'opponent_difficulty'] = fixture['difficulty'].values[0]
            if fixture['H/A'].values[0] == 'A':
                # gw.loc[gw['id'] == id, 'H/A'] = fixture['H/A'].values[0]
                gw.loc[gw['id'] == id, 'H/A'] = 1


if __name__ == "__main__":
    all_fixtures = fpl_funcs.get_fixtures()
    gw_dfs = get_all_gameweeks(5)
    update_gameweek_with_position_and_fixture_information(gw_dfs, all_fixtures)
    gw_1 = gw_dfs[0]
    gw_5 = gw_dfs[4]
    print(gw_1.head())
    print(gw_5.head())
    corr = gw_1.corr()
    print(corr['total_points'].sort_values(ascending=False))
    corr = gw_5.corr()
    print(corr['total_points'].sort_values(ascending=False))
