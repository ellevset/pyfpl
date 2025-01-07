
"""
Get player id based on name
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)

class PlayerId:
    def __init__(self, engine):
        self.engine = engine
        self.df = pd.read_sql_table('players', engine, schema='data')

    def calc(self, df):
        logger.info('PlayerId')
        df = df.merge(self.df.set_index('player_name')[['id']], how='left',
                      left_on='name', right_index=True)

        dfx = df.loc[df.id.isna()]
        N_na = len(dfx)

        if N_na > 0:
            logger.info('Missing {} players. Writing to db'.format(N_na))
            dfx = dfx[['name']].rename(columns={'name': 'player_name'})
            dfx.to_sql('players', self.engine,
                       schema='data', if_exists='append', index=False)
            self.df = pd.read_sql_table('players', self.engine, schema='data')
            self.df = self.calc(df)

            dfx.to_sql('teams', self.engine, schema='data', if_exists='append', index=False)
        return dfx



def make(*args, **kwargs):
    return PlayerId(*args, **kwargs)



