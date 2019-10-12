import fpl_functions as fpl_funcs

master_flag = {
            -1: 'test space',
        }[-1]

if __name__ == '__main__':
    if master_flag == 'test space':
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
