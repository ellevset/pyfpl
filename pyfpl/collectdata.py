#! /home/ellevset/anaconda2/bin/python

import requests
import json
import pandas as pd

player_columns = ['id',
                  'code',
                  'dreamteam_count',
                  'element_type',
                  'first_name',
                  'form',
                  'minutes',
                  'second_name',
                  'total_points',
                  'web_name',
                  'team']

def main(f_players=True):
    if f_players:
        print('Fetching players')
        fetch_players()

    #
    df_players = pd.read_csv('players.csv')

    # List of player ids
    player_ids = df_players['player_id'].tolist()

    # List of data per player, to be concatted later
    df_list = list()

    for player_id in player_ids:
        url = 'https://fantasy.premierleague.com/drf/element-summary/%s' % player_id
        r = requests.get(url)
        data = json.loads(r.text)

        # Make df from the players history
        df_player_data = pd.DataFrame.from_records(data['history'])

        # Drop the id columns as it means something else here
        df_player_data.drop(['id'], axis=1, inplace=True)

        # Add player name etc
        df = df_player_data.merge(df_players, how='left', left_on='element', right_on='player_id')

        df_list.append(df)

    # Dump it out
    pd.concat(df_list).to_csv('player_data_2020.csv', index=False)


def fetch_players():
    # URL for all players
    url = "https://fantasy.premierleague.com/drf/elements/"
    r = requests.get(url)
    data = json.loads(r.text)

    df = pd.DataFrame.from_records(data)
    df = df[player_columns].copy()

    df.rename({'id': 'player_id'}, axis=1, inplace=True)

    # Get the team of the player
    df_teams = pd.read_csv('teams.csv')
    df_teams = df_teams[['id', 'name']].copy()
    df_teams.rename({'id': 'team_id'}, axis=1, inplace=True)
    df = df.merge(df_teams, how='left', left_on='team', right_on='team_id')

    # Write to a csv-file
    df.to_csv('players.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
