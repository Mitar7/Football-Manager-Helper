# Football Manager - Helper
import pandas as pd
import os

flag = 0
df = 0

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
msg = """
    SELECT ONE OF THE FOLLOWING OPTIONS:
    1. Find players based on overall status and nationality
    2. Find players for given release clause minimum and maximum
    3. Find highest rated player of selected country
    4. Find by position and rating
    5. Exit program
"""


def find_by_nationality_and_overall(df):
    nationality = input('Please input player\'s nationality: ')
    overall = int(input('Please input overall rating: '))
    print(df[(df['nationality'] == nationality) & (df['overall'] > overall)]
          [['short_name', 'overall', 'player_positions']])


def find_by_release_clause_eur(df):
    print('All values are in Euros!')
    minimum = int(input('Please input minimum release clause: '))
    maximum = int(input('Please input maximum release clause: '))
    print(df[(df['release_clause_eur'] > minimum) & (df['release_clause_eur'] < maximum)]
          [['long_name', 'overall', 'player_positions', 'release_clause_eur']])


def highest_rated_player_of_selected_nationality(df):
    nationality = input('Please input player\'s nationality: ')
    print(df[(df['nationality'] == nationality)][['long_name', 'overall', 'player_positions']].head(1))


def player_by_position_and_rating(df):
    position = input('Please input player\'s position: ')
    rating = int(input('Please input rating: '))
    print(df[(df['player_positions'] == position) & (df['overall'] > rating)]
          [['long_name', 'overall', 'player_positions']])


def select_fifa():
    global flag
    global df
    fifa = int(input('Please select number of FIFA(15-20): '))
    if 14 < fifa < 21:
        df = pd.read_csv(f'data1/players_{fifa}.csv')
        flag = 1
        main_menu()
    else:
        print('Invalid input')
        select_fifa()


def main_menu():
    if flag == 0:
        select_fifa()
    print(msg)
    x = int(input("Input here: "))
    if x == 1:
        find_by_nationality_and_overall(df)
        enter = input()
        clearConsole()
        main_menu()
    if x == 2:
        find_by_release_clause_eur(df)
        enter = input()
        clearConsole()
        main_menu()
    if x == 3:
        highest_rated_player_of_selected_nationality(df)
        enter = input()
        clearConsole()
        main_menu()
    if x == 4:
        player_by_position_and_rating(df)
        enter = input()
        clearConsole()
        main_menu()
    if x == 5:
        exit()


if __name__ == '__main__':
    main_menu()