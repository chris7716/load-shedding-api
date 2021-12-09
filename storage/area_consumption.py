import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class AreaConsumptionModel(Model):
    __table_name__ = 'area_consumption'
    area_id = columns.UUID(primary_key=True, partition_key=True)
    date = columns.Date(primary_key=True, clustering_order="DESC")
    data_id = columns.UUID(default=uuid.uuid4)
    value = columns.Text()