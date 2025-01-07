
"""
Find matches and push to DB
"""

import sys
import logging

from pyfpl.scrapers.FantasyPremierLeague import Score

logger = logging.getLogger(__name__)


def main(*args, **kwargs):

    # Fetch fixture data
    p = Score()
    df = p.fetch()
    logger.info('Found {} players'.format(len(df)))


def set_argparser(parser):
    parser.description = 'Collecting players'


if __name__ == '__main__':
    main(model=sys.argv[1], fp=sys.argv[2])
