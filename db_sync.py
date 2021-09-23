
from blog.models import Blogs

from service.cassandra_base import CassandraBase

# call schema all schema that you create

CassandraBase.create_table(Blogs)

print("DB SYNC COMPLETE")