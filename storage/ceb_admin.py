import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class CebAdminDataModel(Model):
    __table_name__ = 'ceb_admins'
    email = columns.Text(primary_key=True, partition_key=True)
    ceb_admin_id = columns.UUID(default=uuid.uuid4)
    area_id = columns.UUID()
    name = columns.Text()