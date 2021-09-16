from decouple import config
from cassandra.cqlengine import connection
from cassandra.cqlengine.connection import setup
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import RoundRobinPolicy
from service.log import *
from cassandra.cqlengine import management


class CassandraBase(object):
    db_keyspace = config('KEYSPACE')
    db_host = config('DB_HOST')
    cass_user = config('USER')
    cass_password = config('PASSWORD')

    @classmethod
    def db_connection(cls):
        """
        connect with cassandra db
        """
        auth_provider = PlainTextAuthProvider(username=cls.cass_user, password=cls.cass_password)

        try:
            if connection.session is not None:
                print('\n   Already connected ')
                return "Already Connected"
            else:
                setup([cls.db_host], cls.db_keyspace, auth_provider=auth_provider, protocol_version=4,
                      load_balancing_policy=RoundRobinPolicy())
                return "New Connection"
        except Exception as ex:
            # logger
            Log.general_log(ex, "cassandra_connection_error")
            client = None
            return client

    @classmethod
    def create_table(cls, table):
        db_client = cls.db_connection()
        try:
            sync_schema = management.sync_table(table)
            return sync_schema
        except Exception as ex:
            # logger
            Log.general_log(ex, "cassandra_table_sync_error")
            return None

    @classmethod
    def drop_table(cls, table):
        db_client = cls.db_connection()
        try:
            sync_schema = management.drop_table(table)
            return sync_schema
        except Exception as ex:
            # logger
            Log.general_log(ex, "cassandra_table_drop_error")
            return None


