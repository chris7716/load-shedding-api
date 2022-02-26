from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/consumption"
)


@router.post("/{customer_id}")
async def getConsumption(customer_id: int, value: Optional[str]):
    return {"customer_id": customer_id, "value": value}