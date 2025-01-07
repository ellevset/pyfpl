
import requests
import json
import pandas as pd

from pyfpl.scrapers.BaseScraper import BaseScraper

class Players:
    # URL for all players
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    columns = ['id',
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

    translation = {'web_name': 'player_name'}

    def fetch(self):
        r = requests.get(self.url)
        data = json.loads(r.text)

        df = pd.DataFrame.from_records(data['elements'])
        df = df[self.columns].copy()

        # df.rename({'id': 'player_id'}, axis=1, inplace=True)
        #
        # # Get the team of the player
        # df_teams = pd.read_csv('teams.csv')
        # df_teams = df_teams[['id', 'name']].copy()
        # df_teams.rename({'id': 'team_id'}, axis=1, inplace=True)
        # df = df.merge(df_teams, how='left', left_on='team', right_on='team_id')

        return df


class Teams(BaseScraper):
    # URL for all players
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    json_element = 'teams'
    columns = ['id',
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

    translation = {'web_name': 'player_name'}

    def __init__(self):
        super().__init__()

class Score(BaseScraper):
    # URL for all players
    url = "https://fantasy.premierleague.com/api/fixtures/"
    json_element = 'teams'
    columns = ['id',
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

    translation = {'web_name': 'player_name'}

    def fetch(self):
        r = requests.get(self.url)
        data = json.loads(r.text)
        return pd.DataFrame(data)

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    p = Players()
    df = p.fetch()
    print('kdjfhg')