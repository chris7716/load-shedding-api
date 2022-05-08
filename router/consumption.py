from typing import List, Optional
from fastapi import APIRouter

from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import ConstantSpeculativeExecutionPolicy
from cassandra.query import SimpleStatement

from storage import temp_data

router = APIRouter(
    prefix="/consumption"
)

@router.post("/shed")
async def saveTempData():
    data = temp_data.TempData(load_shedding=False, amount=0)
    data.save()
    return {"value": 0}

@router.post("/consumption")
async def saveTempData(ids: List[str], consumptions: List[str]):
    return {"ids": ids, "consumptions": consumptions}


@router.post("/{customer_id}")
async def getConsumption(customer_id: int, value: Optional[str]):
    data = temp_data.TempData(load_shedding=False, amount=0)
    data.save()
    return {"customer_id": customer_id, "value": value}
