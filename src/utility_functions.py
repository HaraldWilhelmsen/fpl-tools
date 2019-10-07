import numpy as np
import pandas as pd


def team_number_to_name(team_number):
    number_to_name_dictionary = {1: 'Arsenal',
                                 2: 'Aston Villa',
                                 3: 'Bournemouth',
                                 4: 'Brighton & Hove Albion',
                                 5: 'Burnley',
                                 6: 'Chelsea',
                                 7: 'Crystal palace',
                                 8: 'Everton',
                                 9: 'Leicester City',
                                 10: 'Liverpool',
                                 11: 'Manchester City',
                                 12: 'Manchester United',
                                 13: 'Newcastle United',
                                 14: 'Norwich City',
                                 15: 'Sheffield United',
                                 16: 'Southampton',
                                 17: 'Tottenham Hotspur',
                                 18: 'Watford',
                                 19: 'West Ham',
                                 20: 'Wolverhampton Wanderers'}
    return number_to_name_dictionary[team_number]
