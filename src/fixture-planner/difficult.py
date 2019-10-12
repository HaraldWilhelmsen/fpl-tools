import numpy as np
import pandas as pd

def createDataFrame(txt):
    data = pd.read_csv(txt)
    for i in range(1,data.shape[1]):
        for j in range(data.shape[0]):
            num = str(i)
            data[num][j] = data[num][j].split(" ")
    return pd.DataFrame(data = data)
	
df = createDataFrame("fixture_data/difficulty.csv")

# one functon where all teams are evaluted and one where you specify
# which teams to check

def fixture_score_single_team(df, Index, GW_start, GW_end):
    score = 0
    fixture = np.empty(GW_end - GW_start + 1, dtype=object)
    for i in range(GW_start - 1, GW_end): 
        score += int(df.loc[Index][1:][i][2])
        if df.loc[Index][1:][i][1] == 'A':
            fixture[i - GW_start + 1] = df.loc[Index][1:][i][0].lower()
        if df.loc[Index][1:][i][1] == 'H':
            fixture[i - GW_start + 1] = df.loc[Index][1:][i][0].upper()
    return np.array([score, df.loc[Index][0], fixture])


def best_games_future(df, GW_start, GW_end, best_teams):
    number_of_teams = df.shape[0]
    print("number of teams: ", number_of_teams)
    print("from gameweek %i to %i " %(GW_start, GW_end))
    print("Score: Team: Fixtures: ")
    # create an array with size of all teams, which will be sorted by score
    all_teams = np.empty(number_of_teams, dtype = object)
    for teams in range(0, number_of_teams):
        team = fixture_score_single_team(df, teams, GW_start, GW_end)
        print(team[0], " ", team[1], " ", team[2])
        # maybe create a dataframe with score team and fixtures
        all_teams[teams] = team
    # sort the list according to the score
    all_teams = sort_teams_based_on_fixtures(all_teams)
    print("\n Best %i teams with fixtures from GW %i to %i" %(best_teams, GW_start, GW_end))
    for i in range(best_teams):
        print(all_teams[i])
    
def sort_teams_based_on_fixtures(A):
    for i in range(A.size - 1):
        fixture_score = A[i + 1][0]
        team_object = A[i + 1]
        while i >= 0 and A[i][0] > fixture_score:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = team_object
    return A

#best_games_future(df, 1, 3, 3)


