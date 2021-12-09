import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class AreaModel(Model):
    __table_name__ = 'areas'
    status = columns.Text(primary_key=True, partition_key=True)
    area_id = columns.UUID(primary_key=True, partition_key=True, default=uuid.uuid4)
    name = columns.Text()