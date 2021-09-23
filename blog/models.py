from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from service.cassandra_base import CassandraBase


class Blogs(Model):
    id = columns.UUID(primary_key=True)
    title = columns.Text()
    description = columns.Text()
    summery = columns.Text()
    category = columns.Text()
    created_at = columns.DateTime()

    @classmethod
    def create_blog(cls, post_data):
        db_client = CassandraBase.db_connection()

        if db_client:
            data = Blogs.create(**post_data)
            return data
        else:
            return "can not save data"

if __name__ == '__main__':
    initiate_cl= Blogs()

    data = {"title": "test blog", "description":"sfsdfg"}
    print(initiate_cl.create_blog(data))




