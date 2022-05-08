import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class PriorityLevel(Model):
    __table_name__ = 'priority_levels'
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    level = columns.Integer()
    consumption = columns.Integer()