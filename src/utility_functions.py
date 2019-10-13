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

def team_number_to_short_name(team_number):
    number_to_name_dictionary = {1: 'ARS',
                                 2: 'AVL',
                                 3: 'BOU',
                                 4: 'BHA',
                                 5: 'BUR',
                                 6: 'CHE',
                                 7: 'CRY',
                                 8: 'EVE',
                                 9: 'LEI',
                                 10: 'LIV',
                                 11: 'MCI',
                                 12: 'MUN',
                                 13: 'NEW',
                                 14: 'NOR',
                                 15: 'SHU',
                                 16: 'SOU',
                                 17: 'TOT',
                                 18: 'WAT',
                                 19: 'WHU',
                                 20: 'WOL'}
    return number_to_name_dictionary[team_number]

