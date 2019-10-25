import fpl_functions as fpl_funcs
import utility_functions as util_funcs

master_flag = {
            -1: 'test space',
            0: 'create teams',
            1: 'create squad',
            2: 'choose squad',
            3: 'gameweek data',
        }[0]

if __name__ == '__main__':
    if master_flag == 'test space':
        print('Test space')
    elif master_flag == 'create teams':
        team_list = fpl_funcs.create_team_list()

        Arsenal = team_list[0]
        print(Arsenal.name)
        print('Players with most points..')
        print(Arsenal.players_df.sort_values('total_points', ascending=False).head())
        print('First five fixtures..')
        print(Arsenal.fixtures_df.head())

        Wolves = team_list[-1]
        print(Wolves.name)
        print('Players with most points..')
        print(Wolves.players_df.sort_values('total_points', ascending=False).head())
        print('First five fixtures..')
        print(Wolves.fixtures_df.head())

    elif master_flag == 'create squad':
        # list of my current players
        list_of_player_names = ['Patrício', 'Pope', 'Alexander-Arnold', 'Rico', 'Pereira', 'Mount', 'Lundstram',
                                'McGinn', 'Yarmolenko', 'Mané', 'Abraham', 'Vardy', 'Aubameyang', 'Söyüncü',
                                'Dendoncker']
        list_of_player_teams = [20, 5, 10, 3, 9, 6, 15, 2, 19, 10, 6, 9, 1, 9, 20]
        example_squad = fpl_funcs.create_fpl_squad(list_of_player_names, list_of_player_teams)
        print(example_squad.players_df)

    elif master_flag == 'choose squad':
        choice_attribute = 'total_points'
        fpl_funcs.choose_squad_based_on_attribute(choice_attribute)

    elif master_flag == 'gameweek data':
        fpl_funcs.get_gameweek_data(1)
