
"""
Add column with given value
"""

import pandas as pd

class AddColumnValue:
    def __init__(self, column, value, dtype=str, *args, **kwargs):
        """

        """
        self.column = column
        self.dtype = dtype
        self.value = value

    def __str__(self):
        return 'AddColumnValue'

    def calc(self, df):
        df[self.column] = self.dtype(self.value)
        return df


def make(*args, **kwargs):
    return AddColumnValue(*args, **kwargs)



