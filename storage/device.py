import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class DeviceModel(Model):
    __table_name__ = 'devices'
    device_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    customer_id = columns.UUID(primary_key=True, partition_key=True)
    device_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)