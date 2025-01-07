
"""
Rename a column
"""

import pandas as pd

class RenameColumn:
    def __init__(self, *args, **kwargs):
        """

        """
        self.columns = kwargs

    def __str__(self):
        return 'Rename'

    def calc(self, df):
        df = df.rename(columns=self.columns)
        return df


def make(*args, **kwargs):
    return RenameColumn(*args, **kwargs)



