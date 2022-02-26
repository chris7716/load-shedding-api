from typing import Optional
from fastapi import APIRouter

router = APIRouter()


@router.post("/consumption/{customer_id}")
async def getConsumption(customer_id: int, value: Optional[str]):
    return {"customer_id": customer_id, "value": value}