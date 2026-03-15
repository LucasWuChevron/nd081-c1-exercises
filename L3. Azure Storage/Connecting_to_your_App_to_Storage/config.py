import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world-123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-word-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!!Jenny1022'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'lucasblob'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '/TQR+G9dLp8KLTREuGPtfdalDXLowyd3YYxQTKjdUDeab/gqSWPf9jiVSD6laKfs+GDPaHcd460V+AStifeiAw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
