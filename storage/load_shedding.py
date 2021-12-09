import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class LoadSheddingModel(Model):
    __table_name__ = 'load_sheddings'
    area_id = columns.UUID(primary_key=True, partition_key=True, default=uuid.uuid4)
    status = columns.Text(primary_key=True, partition_key=True)
    id = columns.UUID(default=uuid.uuid4)
    from_time = columns.DateTime()
    to_time = columns.DateTime()