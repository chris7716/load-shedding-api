import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class UserModel(Model):
    __table_name__ = 'users'
    email = columns.Text(primary_key=True, partition_key=True)
    password = columns.Text(primary_key=True, partition_key=True)
    id = columns.UUID(default=uuid.uuid4)