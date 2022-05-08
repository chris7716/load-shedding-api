import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class TempCustomer(Model):
    __table_name__ = 'temp_customer'
    id = columns.Text(primary_key=True)
    amount = columns.Integer()
    ready = columns.Boolean()
    priority = columns.Integer()