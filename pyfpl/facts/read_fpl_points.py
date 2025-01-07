
"""
Read FPL data dump files
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class TeamId:
    def __init__(self, fp):
        self.df = pd.read_csv(fp)
        self.columns = ['position', 'clean_sheets', 'creativity', 'fixture', 'bonus',
                        'goals_scored', 'minutes', 'own_goals', 'penalties_missed',
                        'penalties_saved', 'red_cards', 'round', 'saves', 'starts',
                        'total_points',  'value', 'was_home', 'yellow_cards']

    def calc(self, df):
        logger.info('Reading FPL data')
        return self.df


def make(*args, **kwargs):
    return TeamId(*args, **kwargs)



