import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class SuperAdminModel(Model):
    __table_name__ = 'super_admins'
    email = columns.Text(primary_key=True, partition_key=True)
    super_admin_id = columns.UUID(default=uuid.uuid4)
    name = columns.Text()