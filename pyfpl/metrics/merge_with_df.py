
"""
Extract data from database
"""

import pandas as pd

class MergeWithDf():
    def __init__(self, df, left_on, right_on, *args, **kwargs):
        """

        """
        self.df = df
        self.left_on = left_on
        self.right_on = right_on


    def __str__(self):
        return 'MergeWithDf'

    def calc(self, df):
        df = df.merge(self.df, how='left',
                      right_on=self.right_on, left_on=self.left_on)
        return df


def make(*args, **kwargs):
    return MergeWithDf(*args, **kwargs)



