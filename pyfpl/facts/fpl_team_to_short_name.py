
"""
Add short-name home/away
"""

import logging

import json
import pandas as pd
import requests

logger = logging.getLogger(__name__)


class FplTeamToShortName:
    def __init__(self, fp, colname):
        self.df = pd.read_csv(fp)
        self.colname = colname
        self.colname_new = 'short_name_{}'.format(colname)

        self.columns = [self.colname_new]

    def calc(self, df):
        logger.info('Team ID FPL')
        dfx = self.df.set_index('id')[['short_name']].rename(columns={'short_name': self.colname_new})
        df = df.merge(dfx, how='left', left_on=self.colname, right_index=True)

        return df


def make(*args, **kwargs):
    return FplTeamToShortName(*args, **kwargs)



