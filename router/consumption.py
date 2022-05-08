from typing import List, Optional
from fastapi import APIRouter

from service import load_shedding_service

from storage import temp_data
from storage import temp_customer
from storage import priority_level

router = APIRouter(
    prefix="/consumption"
)

@router.post("/")
async def saveTempData(ids: List[str], consumptions: List[str]):
    return {"ids": ids, "consumptions": consumptions}

# @router.post("/{customer_id}")
# async def getConsumption(customer_id: int, value: Optional[str]):
#     data = temp_data.TempData(load_shedding=False, amount=0)
#     data.save()
#     return {"customer_id": customer_id, "value": value}

@router.get("/shed/start")
async def saveTempData(amount: int):
    data = temp_data.TempData(data_id='536f45e3-fdda-4136-8334-b3bfe6dae370', load_shedding=True, amount=amount)
    data.save()
    return load_shedding_service.shed_load(1)

@router.post("/shed/stop")
async def saveTempData():
    data = temp_data.TempData(data_id='536f45e3-fdda-4136-8334-b3bfe6dae370', load_shedding=False, amount=0)
    data.save()
    return {"value": 0}

@router.get("/shed/status")
async def saveTempData():
    data = temp_data.TempData.get(data_id='536f45e3-fdda-4136-8334-b3bfe6dae370')
    return {"load_shedding": data.load_shedding}

@router.post("/save")
async def saveTempData(ids: List[str], consumptions: List[int]):
    size = len(ids)
    for i in range(0, size):
        data = temp_customer.TempCustomer(id=ids[i], amount=consumptions[i], ready=False)
        data.save()
    return load_shedding_service.shed_load(1, consumptions)

@router.post("/save/priorities")
async def savePriorities(levels: List[int], consumptions: List[int]):
    for i in range(0, len(levels)):
        data = priority_level.PriorityLevel(level=levels[i], consumption=consumptions[i])
        data.save()
    return {"success": True}