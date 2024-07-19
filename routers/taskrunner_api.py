from fastapi import APIRouter, Request
import logging
from controllers.taskrunner import task


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/taskrunner",
    tags=["api/taskrunner"],
)


@router.get("/")
async def index():
    return {"message": "Task Runner API"}


@router.post("/task")
async def task(request: Request):
    return task(request=request)

