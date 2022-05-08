import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class TempData(Model):
    __table_name__ = 'temp_data'
    data_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    load_shedding = columns.Boolean()
    amount = columns.Integer()