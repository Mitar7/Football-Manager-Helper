# Football Manager - Helper

import pandas as pd

df = pd.read_csv('data/players_20.csv')


def find_by_nationality_and_overall():
    nationality = input('Please input player\'s nationality: ')
    overall = int(input('Please input overall rating: '))
    print(df[(df['nationality'] == nationality) & (df['overall'] > overall)]
          [['short_name', 'overall', 'player_positions']])


def find_by_release_clause_eur():
    print('All values are in Euros!')
    minimum = int(input('Please input minimum release clause: '))
    maximum = int(input('Please input maximum release clause: '))
    print(df[(df['release_clause_eur'] > minimum) & (df['release_clause_eur'] < maximum)]
          [['short_name', 'overall', 'player_positions', 'release_clause_eur']])

