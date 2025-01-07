
"""
Extract data from database
"""

import pandas as pd

class GetFromDb():
    def __init__(self, table, left_id, right_id, engine, *args, **kwargs):
        """

        """
        self.table = table
        self.left_id = left_id
        self.right_id = right_id
        self.engine = engine

        with engine.connect() as conn:
            self.df = pd.read_sql_table(self.table, conn, schema='data')

    def __str__(self):
        return 'GetFromDb'

    def calc(self, df):
        df = df.merge(self.df, how='left',
                      right_on=self.right_id, left_on=self.left_id)
        return df


def make(*args, **kwargs):
    return GetFromDb(*args, **kwargs)



