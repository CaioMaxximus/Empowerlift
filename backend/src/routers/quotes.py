from fastapi import APIRouter
from src.services import quote_service

router = APIRouter(
    prefix ='/qoutes'
)

@router.get("/")
def get_random_quote():
    return  quote_service.get_random_quote()