
"""
Script to convert

"""

import logging

logger = logging.getLogger(__name__)

from pyfpl.scrapers.FantasyPremierLeague import Players, Teams

def main(*args, **kwargs):
    p = Teams()

    df = p.fetch()
    logger.info('Found {} players'.format(len(df)))


def set_argparser(parser):
    parser.description = 'Collecting players'


if __name__ == '__main__':
    main(model=sys.argv[1], fp=sys.argv[2])
