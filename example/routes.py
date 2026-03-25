"""
Example route used for the minimality-check experiment.
Bug: POST /items returns 200 instead of 201.
"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/items")
def create_item(name: str):
    """Create a new item. Should return 201, but returns 200 (bug)."""
    return {"name": name, "created": True}
