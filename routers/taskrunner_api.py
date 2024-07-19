from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
import logging


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/taskrunner",
    tags=["api/taskrunner"],
)


@router.get("/")
async def index():
    return {"message": "Task Runner API"}





