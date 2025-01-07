
"""
Check if row is in db table
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

class ExistsInDb:
    def __init__(self, table, columns, engine, *args, **kwargs):
        """

        """
        self.table = table
        self.columns = columns
        self.engine = engine

    def __str__(self):
        return 'ExistsInDb'

    def check_in_db(self, session, *args, **kwargs):
        exists = True
        try:
            session.query(self.table).filter_by(**kwargs).one()
            exists = True
        except NoResultFound:
            exists = False
        except MultipleResultsFound:
            exists = False
        return exists

    def calc(self, df):
        with Session(self.engine) as session:
            df['exists'] = df.apply(lambda r: self.check_in_db(session, **r[self.columns]), axis=1)
        return df


def make(*args, **kwargs):
    return ExistsInDb(*args, **kwargs)



