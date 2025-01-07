
"""
Rename a column
"""

import pandas as pd

class RenameColumn():
    def __init__(self, name, new_name, *args, **kwargs):
        """

        """
        self.name = name
        self.new_name = new_name

    def __str__(self):
        return 'Rename'

    def calc(self, df):
        df = df.rename(columns={self.name: self.new_name})
        return df


def make(*args, **kwargs):
    return RenameColumn(*args, **kwargs)



