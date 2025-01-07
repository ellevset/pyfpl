
"""
Add team id from short name
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class FixturesFromCsv:
    def __init__(self, fp):
        self.df = pd.read_csv(fp)
        self.columns = ['fixture_id', 'kickoff_time', 'team_a_score', 'team_h_score']

    def calc(self, df):
        logger.info('Reading fixtures')
        self.df = self.df.rename(columns={'id': 'fixture_id'})
        return self.df


def make(*args, **kwargs):
    return FixturesFromCsv(*args, **kwargs)



