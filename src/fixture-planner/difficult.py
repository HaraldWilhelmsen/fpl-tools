import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def create_data_frame(txt):
    data = pd.read_csv(txt)
    for i in range(1,data.shape[1]):
        for j in range(data.shape[0]):
            num = str(i)
            data[num][j] = data[num][j].split(" ")

    return pd.DataFrame(data = data)
	
df = create_data_frame("fixture_data/difficulty.csv")

def fixture_score_one_team(df, team_idx, GW_start, GW_end):
    score = 0
    team = df.loc[team_idx][0]
    upcoming_fixtures = np.empty(GW_end - GW_start + 1, dtype=object)
    for i in range(GW_start - 1, GW_end): 
        score += int(df.loc[team_idx][1:][i][2])
        if df.loc[team_idx][1:][i][1] == 'A':
            upcoming_fixtures[i - GW_start + 1] = df.loc[team_idx][1:][i][0].lower()
        if df.loc[team_idx][1:][i][1] == 'H':
            upcoming_fixtures[i - GW_start + 1] = df.loc[team_idx][1:][i][0].upper()
    return np.array([score, team, upcoming_fixtures])

def best_games_future(df, GW_start, GW_end, best_teams):
    number_of_teams = df.shape[0]
    print("number of teams: ", number_of_teams)
    print("from gameweek %i to %i " %(GW_start, GW_end))
    print("Score: Team: Fixtures: ")
    # create an array with size of all teams, which will be sorted by score
    all_teams = np.empty(number_of_teams, dtype = object)
    for teams in range(0, number_of_teams):
        team = fixture_score_one_team(df, teams, GW_start, GW_end)
        print(team[0], " ", team[1], " ", team[2])
        # maybe create a dataframe with score team and fixtures
        all_teams[teams] = team
    # sort the list according to the score
    all_teams = insertionsort(all_teams)
    print("\n Best %i teams with fixtures from GW %i to %i" %(best_teams, GW_start, GW_end))
    for i in range(best_teams):
        print(all_teams[i])
    return all_teams

def insertionsort(A):
    # sort an array according to its fixture score
    for i in range(A.size - 1):
        score = A[i + 1][0]
        team_array = A[i + 1]
        while i >= 0 and A[i][0] > score:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = team_array
    return A

#best_games_future(df, 1, 3, 3)
# add difficult value and fixture together ars 5, new 4

def visualize_fixtures(df, GW_start, GW_end):
    info = fixture_score_one_team(df, 1, GW_start, GW_end)
    fix = info[2]
    diff = np.random.randint(1, 5, (len(fix)))
    print(diff)
    fig, ax = plt.subplots(1,1)


    ax.imshow([diff]) 
    #c = ax.pcolor([diff])
    plt.show()

visualize_fixtures(df, 1, 4)
