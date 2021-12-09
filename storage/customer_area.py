import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class CustomerAreaModel(Model):
    __table_name__ = 'customer_areas'
    area_id = columns.UUID(primary_key=True, partition_key=True)
    customer_id = columns.UUID()