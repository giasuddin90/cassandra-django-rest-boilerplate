from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Blogs(Model):
    id = columns.UUID(primary_key=True)
    title = columns.Text()
    description = columns.Text()
    summery = columns.Text()
    category = columns.Text()
    created_at = columns.DateTime()



