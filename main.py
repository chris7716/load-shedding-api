from functools import lru_cache
from typing import Optional
from fastapi import Depends, FastAPI
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.connection import setup

from router import consumption
from router import customer
from config import settings

from storage import area_consumption
from storage import area
from storage import ceb_admin
from storage import customer_area
from storage import customer_daily_summary
from storage import customer_data
from storage import customer_priority
from storage import device_daily_summary
from storage import device_data
from storage import device
from storage import load_shedding
from storage import super_admin
from storage import user
from storage import temp_data
from storage import temp_customer
from storage import priority_level

app = FastAPI()

setup([settings.db_server], settings.db_cluster, retry_connect=True)

sync_table(area_consumption.AreaConsumptionModel)
sync_table(area.AreaModel)
sync_table(ceb_admin.CebAdminDataModel)
sync_table(customer_area.CustomerAreaModel)
sync_table(customer_daily_summary.CustomerDailySummaryModel)
sync_table(customer_data.CustomerDataModel)
sync_table(customer_priority.CustomerPriorityModel)
sync_table(device_daily_summary.DeviceDailySummaryModel)
sync_table(device_data.DeviceDataModel)
sync_table(device.DeviceModel)
sync_table(load_shedding.LoadSheddingModel)
sync_table(super_admin.SuperAdminModel)
sync_table(user.UserModel)
sync_table(temp_data.TempData)
sync_table(temp_customer.TempCustomer)
sync_table(priority_level.PriorityLevel)

@app.get("/")
async def root():
    #em1 = example.ExampleModel.create(example_type=0, description="example1", created_at=datetime.now())
    return {"message": "Hello World"}

# Consumption Data Endpoint
app.include_router(consumption.router)

# Customer Data Endpoint
app.include_router(customer.router)