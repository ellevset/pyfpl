

"""
Find the numbe of goals scored in the last three matches

"""


class Goals_last_three():
    def __init__(self, df):
        self.df_goals = df.groupby(['team_id', 'round']).sum()['goals_scored'].reset_index()
        self.columns = ['goals_last_three']

    def generate(self, df):
        df['goals_last_three'] = df.apply(self.goals, axis=1)
        return df

    def goals(self, row):
        # The rounds we are looking at
        rounds = [i for i in range(row['round'] - 3, row['round']) if i > 0]

        return self.df_goals.loc[(self.df_goals.team_id == row.opponent_team) &
                                 (self.df_goals['round'].isin(rounds))]['goals_scored'].sum()

def generate(df):
    g = Goals_last_three(df)
    return g.generate(df), g.columns



