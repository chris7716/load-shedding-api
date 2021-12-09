import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class CustomerPriorityModel(Model):
    __table_name__ = 'customer_priorities'
    priority_index = columns.Text(primary_key=True, partition_key=True)
    area_id = columns.UUID(primary_key=True, partition_key=True)
    customer_id = columns.UUID()