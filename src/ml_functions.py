import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

import fpl_functions as fpl_funcs
import utility_functions as util_funcs


def get_all_gameweeks(latest_gameweek):
    df = pd.DataFrame()
    for i in range(1, latest_gameweek+1):
        gameweek_df = fpl_funcs.get_gameweek_data(i)
        gameweek_df.loc[:, 'gameweek'] = i
        df = df.append(gameweek_df, ignore_index=True)
    return df


def update_gameweeks_with_position(gameweeks_df):
    gameweeks_df.loc[:, 'position'] = 0
    ids = np.unique(gameweeks_df['id'].values)
    for player_id in ids:
        position = util_funcs.get_position_from_player_id(player_id)
        gameweeks_df.loc[gameweeks_df['id'] == player_id, 'position'] = position


def update_gameweeks_with_fixture_information(gameweeks_df, fixtures, starting_gameweek=5):
    gameweeks_df.loc[:, 'opponent_difficulty'] = 0
    gameweeks_df.loc[:, 'H/A'] = 0
    gameweeks = np.unique(gameweeks_df['gameweek'].values)
    boolean = gameweeks >= starting_gameweek
    gameweeks_to_update = gameweeks[boolean]
    for gameweek in gameweeks_to_update:
        ids = gameweeks_df.loc[gameweeks_df['gameweek'] == gameweek, 'id'].values
        for player_id in ids:
            fixture = util_funcs.get_gameweek_information(player_id, gameweek, fixtures)
            gameweeks_df.loc[(gameweeks_df['id'] == player_id) & (gameweeks_df['gameweek'] == gameweek),
                             'opponent_difficulty'] = fixture['difficulty'].values[0]
            if fixture['H/A'].values[0] == 'A':
                # H -> 0, A -> 1
                gameweeks_df.loc[(gameweeks_df['id'] == player_id) & (gameweeks_df['gameweek'] == gameweek),
                                 'H/A'] = 1


def update_gameweeks_with_expected_statistics(gameweeks_df, starting_gameweek=5, prev_gameweeks_to_use=4):
    gameweeks_df.loc[:, 'xG'] = 0  # Expected goals. Average number of goals last 4 gws
    gameweeks_df.loc[:, 'xA'] = 0  # Expected assists. As the average number of assists last 4 gws
    gameweeks_df.loc[:, 'xCS'] = 0  # Expected probability of clean sheet. Average number of CS last 4 gws
    gameweeks_df.loc[:, 'xICT'] = 0  # Expected ICT. As the average ICT last 4 gws
    gameweeks_df.loc[:, 'xP'] = 0  # Expected points/form. Average points last 4 gws
    gameweeks_df.loc[:, 'xM'] = 0  # Expected minutes. Average minutes last 4 gws
    gameweeks_df.loc[:, 'xS'] = 0  # Expected saves. Average saves last 4 gws
    stats_to_use = ['total_points', 'goals_scored', 'assists', 'clean_sheets', 'ict_index', 'minutes', 'saves', 'gameweek']
    gameweeks = np.unique(gameweeks_df['gameweek'].values)
    boolean = gameweeks >= starting_gameweek
    gameweeks_to_update = gameweeks[boolean]
    for gameweek in gameweeks_to_update:
        ids = gameweeks_df.loc[gameweeks_df['gameweek'] == gameweek, 'id'].values
        for player_id in ids:
            player_stats = gameweeks_df.loc[gameweeks_df['id'] == player_id, stats_to_use].copy()
            player_stats_to_use = player_stats.loc[(player_stats['gameweek'] < gameweek) & (player_stats['gameweek'] >= (gameweek-prev_gameweeks_to_use))]
            if len(player_stats_to_use) > 0:
                avg_values = player_stats_to_use.mean().to_dict()

                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xP'] = avg_values['total_points']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xG'] = avg_values['goals_scored']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xA'] = avg_values['assists']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xCS'] = avg_values['clean_sheets']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xICT'] = avg_values['ict_index']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xM'] = avg_values['minutes']
                gameweeks_df.loc[(gameweeks_df['gameweek'] == gameweek) & (gameweeks_df['id'] == player_id), 'xS'] = avg_values['saves']


def pre_processing(latest_gameweek, starting_gameweek=5):
    all_fixtures = fpl_funcs.get_fixtures()
    gws_df = get_all_gameweeks(latest_gameweek)
    update_gameweeks_with_position(gws_df)
    update_gameweeks_with_fixture_information(gws_df, all_fixtures, starting_gameweek=starting_gameweek)
    update_gameweeks_with_expected_statistics(gws_df, starting_gameweek=starting_gameweek, prev_gameweeks_to_use=4)
    return gws_df


def rf_model(parameters):
    if parameters is None:
        return RandomForestRegressor()


def train_model(data, features_to_use, train_label, model_parameters=None):
    train_data = data[features_to_use]
    train_labels = data[train_label]
    model = rf_model(model_parameters)
    model.fit(train_data, train_labels)
    return model


def test_model(model, data, features_to_use):
    test_data = data[features_to_use]
    predictions = model.predict(test_data)
    return predictions


def train_and_test_model(latest_gameweek, starting_gameweek=5):
    gws_df = pre_processing(latest_gameweek, starting_gameweek)
    features_to_use = ['xG', 'xA', 'xM', 'xS', 'xICT', 'xCS', 'opponent_difficulty', 'H/A']
    train = gws_df.loc[(gws_df['gameweek'] < latest_gameweek) & (gws_df['gameweek'] >= starting_gameweek)]
    train = train[train['minutes'] > 10]
    test = gws_df.loc[gws_df['gameweek'] == latest_gameweek]
    test = test[test['minutes'] > 10]
    model = train_model(train, features_to_use, 'total_points')
    predictions = test_model(model, test, features_to_use)
    test.loc[:, 'prediction_points'] = predictions
    print(f"mae: {np.mean(np.abs(predictions-test['total_points'].values))}")

    ids = test['id'].values

    #plt.plot(ids, predictions, '.-', alpha=0.5, label='Prediction')
    #plt.plot(ids, test['total_points'].values, alpha=0.5, label='Total points')
    plt.plot(ids, np.abs(test['total_points'].values-predictions), alpha=0.5)
    plt.ylabel('|Total points - predicted points|')
    plt.xlabel('Player id')
    # plt.legend()
    plt.show()

    ids_to_look_at = test.sort_values('prediction_points', ascending=False)['id'].values[:10]
    names = []
    for player_id in ids_to_look_at:
        names.append(util_funcs.get_name_from_player_id(player_id))
    print(names)


if __name__ == "__main__":
    # updated_gws_df = pre_processing(5, starting_gameweek=5)
    #
    # gw_1 = updated_gws_df.loc[(updated_gws_df['gameweek'] == 1) & (updated_gws_df['minutes'] > 60)]
    # gw_5 = updated_gws_df.loc[(updated_gws_df['gameweek'] == 5) & (updated_gws_df['minutes'] > 60)]
    # print(gw_1.head())
    # print(gw_5.head())
    # corr = gw_1.corr()
    # print(corr['total_points'].sort_values(ascending=False))
    # corr = gw_5.corr()
    # print(corr['total_points'].sort_values(ascending=False))

    train_and_test_model(8)
