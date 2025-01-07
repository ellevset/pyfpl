
from sqlalchemy import create_engine


def get_engine():
    return create_engine("postgresql+psycopg2://pel:grandiosa@192.168.10.108:5432/fpl")