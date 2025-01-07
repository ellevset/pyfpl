

"""
Add basis data like player info and points
"""


class PlayerData():
    def __init__(self, df):
        self.columns = ['player_id', 'web_name', 'total_points_x']

    def generate(self, df):
        #df = df[self.columns]
        df.rename({'total_points_x': 'points'})
        return df

def generate(df):

    g = PlayerData(df)
    return g.generate(df), g.columns



