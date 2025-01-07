
import requests
import json
import pandas as pd


class BaseScraper:
    # URL for all players
    url = None
    json_element = 'tyui'


    def fetch(self):
        r = requests.get(self.url)
        data = json.loads(r.text)

        df = pd.DataFrame.from_records(data[self.json_element])
        return df

    def translate(self, code=None):
        pass
        # translations = {'fpl': }
        ## Write to a csv-file
        #df.to_csv('players.csv', encoding='utf-8', index=False)