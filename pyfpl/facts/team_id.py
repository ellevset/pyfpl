
"""
Add team id from short name
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class TeamId:
    def __init__(self, engine, colname, newcolname):
        self.engine = engine
        self.df = pd.read_sql_table('teams', engine, schema='data')
        self.colname = colname
        self.newcolname = newcolname
        self.columns = [self.newcolname]


    def calc(self, df):
        logger.info('Team ID')

        if self.newcolname in df.columns:
            df = df.drop(columns=self.newcolname)
        dfx = self.df.set_index('short_name')[['id']].rename(columns={'id': self.newcolname})
        df = df.merge(dfx, how='left', left_on=self.colname, right_index=True)

        return df


def make(*args, **kwargs):
    return TeamId(*args, **kwargs)



