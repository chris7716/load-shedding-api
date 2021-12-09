import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class CustomerDataModel(Model):
    __table_name__ = 'customer_data'
    email = columns.Text(primary_key=True, partition_key=True)
    area_id = columns.UUID(primary_key=True, partition_key=True)
    customer_id = columns.UUID(default=uuid.uuid4)
    priority_index = columns.Text()
    status = columns.Text()
    tariff_type = columns.Text()
    name = columns.Text()
    current = columns.Text()
    voltage = columns.Text()
    tariff = columns.Text()