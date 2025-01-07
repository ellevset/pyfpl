
"""
Keep rows based on column value
"""


class FilterOnColumn:
    def __init__(self, column, value, *args, **kwargs):
        """

        """
        self.column = column
        self.value = value

    def __str__(self):
        return 'FilterOnColumn'

    def calc(self, df):
        df = df.loc[df[self.column] == self.value].copy()
        return df


def make(*args, **kwargs):
    return FilterOnColumn(*args, **kwargs)



