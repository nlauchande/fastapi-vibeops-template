"""
Example route used for the minimality-check experiment.
Fix: POST /items correctly returns 201.
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/items", status_code=201)
def create_item(name: str):
    """Create a new item. Returns 201 Created."""
    return {"name": name, "created": True}
