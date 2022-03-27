from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/customer"
)


@router.post("/")
async def getCustomer():
    return {"customer_id": "1"}