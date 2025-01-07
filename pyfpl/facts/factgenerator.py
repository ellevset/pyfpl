
"""
Class steering the fact generation

"""

import importlib

import pandas as pd

#from pyfpl.facts.goals_last_three import goals_last_three

class FactGenerator():

    def __init__(self):
        self.df = pd.read_csv('player_data.csv')

    def generate(self):

        facts = ['playerdata', 'goals_last_three']
        columns = []

        for fct in facts:
            module = importlib.import_module('pyfpl.facts.%s' % fct)

            self.df, c = module.generate(self.df)
            columns.extend(c)

        return self.df[columns]


if __name__ == '__main__':

    fg = FactGenerator()
    #df = goals_last_three(fg.df)
    df = fg.generate()
    df.to_csv('facts.csv', index=False)




