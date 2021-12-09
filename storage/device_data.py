import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class DeviceDataModel(Model):
    __table_name__ = 'device_data'
    customer_id = columns.UUID(primary_key=True, partition_key=True)
    device_id = columns.UUID(primary_key=True)
    time = columns.DateTime(primary_key=True, clustering_order="DESC")
    data_id = columns.UUID(default=uuid.uuid4)
    value = columns.Text()