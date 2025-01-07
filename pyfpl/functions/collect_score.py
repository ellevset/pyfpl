
"""
Script to write FPL data to db
"""

import sys
import logging
import importlib

from pyfpl.dbutils import get_engine
from pyfpl.scrapers.FantasyPremierLeague import Score, Teams

logger = logging.getLogger(__name__)


def main(*args, **kwargs):

    # Get an engine to connect to db
    engine = get_engine()

    # Get teams so we can extract the shortname
    df_teams = Teams().fetch()
    df_teams = df_teams[['id', 'short_name']].rename(columns={'id': 'fpl_team_id'})

    # Fetch fixture data
    p = Score()
    df = p.fetch()

    #df = df.merge(df_teams.rename(columns={'short_name': 'shortname_h'}),
    #              left_on='team_h', right_on='id')
    #df = df.merge(df_teams.rename(columns={'short_name': 'shortname_a'}),
    #              left_on='team_a', right_on='id')

    my_metrics = [('rename_columns', {'name': 'id', 'new_name': 'fixture_id'}),
                  ('merge_with_df', {'df': df_teams, 'left_on': 'team_h', 'right_on': 'fpl_team_id'}),
                  ('rename_columns', {'name': 'short_name', 'new_name': 'shortname_h'}),
                  ('get_from_db', {'table': 'teams', 'engine': engine,
                                   'left_id': 'shortname_h', 'right_id': 'short_name'}),
                  ('merge_with_df', {'df': df_teams, 'left_on': 'team_a', 'right_on': 'fpl_team_id'}),
                  ('rename_columns', {'name': 'short_name', 'new_name': 'shortname_a'}),
                  ('get_from_db', {'table': 'teams', 'engine': engine,
                                   'left_id': 'shortname_a', 'right_id': 'short_name'}),
                  ]
    metrics_to_run = []
    for m in my_metrics:
        c = importlib.import_module('metrics.{}'.format(m[0]))
        logger.info(c)
        metrics_to_run.append(c.make(**m[1]))

    for m in metrics_to_run:
        logger.info(m)
        df = m.calc(df)
    logger.info('Found {} players'.format(len(df)))


def set_argparser(parser):
    parser.description = 'Collecting players'


if __name__ == '__main__':
    main(model=sys.argv[1], fp=sys.argv[2])
