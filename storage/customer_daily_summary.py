import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class CustomerDailySummaryModel(Model):
    __table_name__ = 'customer_daily_summaries'
    customer_id = columns.UUID(primary_key=True, partition_key=True)
    date = columns.Date(primary_key=True, clustering_order="DESC")
    data_id = columns.UUID(default=uuid.uuid4)
    value = columns.Text()