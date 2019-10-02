import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors

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
    upcoming_fixtures_score = np.empty(GW_end - GW_start + 1, dtype=int)
    for i in range(GW_start - 1, GW_end): 
        score += int(df.loc[team_idx][1:][i][2])
        if df.loc[team_idx][1:][i][1] == 'A':
            upcoming_fixtures[i - GW_start + 1] = df.loc[team_idx][1:][i][0].lower()
        if df.loc[team_idx][1:][i][1] == 'H':
            upcoming_fixtures[i - GW_start + 1] = df.loc[team_idx][1:][i][0].upper()
        upcoming_fixtures_score[i - GW_start + 1] = int(df.loc[team_idx][1:][i][2])
    return np.array([score, team, upcoming_fixtures, upcoming_fixtures_score])

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

def visualize_one_teams_fixtures(df, GW_start, GW_end, team):
    team_index = df.loc[df['Team']=='AVL'].index[0]
    info = fixture_score_one_team(df, team_index, GW_start, GW_end)
    diff = info[3]
    # info should be a list of objects 
    x_len, y_len = GW_end-GW_start+1, 1
    fig, ax = plt.subplots(1,1)
    
    # add x-axis 
    gameweeks = np.empty([x_len], dtype=object)
    for j, i in enumerate(np.arange(GW_start, GW_end + 1)):
        gameweeks[j] = 'GW' + ' ' + str(i)
      
    
    # plot values for each pixel
    for j in range(x_len):
            text = ax.text(j, 0, info[2][j], ha="center", va="center", color="black")

    cmap = colors.ListedColormap(["lime", "forestgreen", "lightgrey", "lightcoral", "red"])
    img = plt.imshow([diff], cmap=cmap)
    ax.set_xticks(np.arange(x_len))
    ax.set_xticklabels(gameweeks)
    ax.set_yticks(np.arange(y_len))
    ax.set_yticklabels(np.array([team], dtype=object))
    fig.tight_layout()
    ax.set_title("Fixture plan from GW %i to GW %i" %(GW_start, GW_end))
    plt.show()

def visualize_fixtures(df, GW_start, GW_end):
    info = np.empty(df.shape[0], dtype=object)
    diff = np.empty([df.shape[0], GW_end - GW_start + 1], dtype=int)
    for i in range(df.shape[0]):
        info[i] = fixture_score_one_team(df, i, GW_start, GW_end)
        diff[i] = info[i][3]
    # info should be a list of objects 
    x_len, y_len = GW_end-GW_start+1, df.shape[0]
    fig, ax = plt.subplots(1,1)
    
    # add x-axis
    
    gameweeks = np.empty([x_len], dtype=object)
    for j, i in enumerate(np.arange(GW_start, GW_end + 1)):
        gameweeks[j] = 'GW' + ' ' + str(i)
    
    # add y-axis
    team = np.empty([y_len+1], dtype=object)
    for i in range(y_len):
        team[i+1] = info[i][1]
   
    # plot values for each pixel
    for i in range(y_len):
        for j in range(x_len):
            text = ax.text(j, i, info[i][2][j], ha="center", va="center", color="black")

    cmap = colors.ListedColormap(["lime", "forestgreen", "lightgrey", "lightcoral", "red"])
    img = plt.imshow(np.array(diff), cmap=cmap)
    ax.set_xticks(np.arange(x_len))
    ax.set_xticklabels(gameweeks)
    #ax.set_yticks(np.arange(y_len))
    ax.set_yticklabels(team)
    fig.tight_layout()
    ax.set_title("Fixture plan from GW %i to GW %i" %(GW_start, GW_end))
    plt.show()

#visualize_one_teams_fixtures(df, 3, 6, 'AVL')
#visualize_fixtures(df, 1,5)

