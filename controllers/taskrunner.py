from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)


async def task(request: Request):
    try:
        incoming_data = await request.json()
        logger.info("incoming_data %s", incoming_data)

        task_type = incoming_data["task_type"]
        code = incoming_data["code"]
        res_cpu = incoming_data["resources"]["cpu"]
        res_gpu = incoming_data["resources"]["gpu"]
        res_ram = incoming_data["resources"]["ram"]
        res_store = incoming_data["resourcs"]["storage"]

    except Exception as e:
        logger.error("Inputs is invalid")
        return JSONResponse(content={"message":"failed", "result":""}, status_code=status.HTTP_400_BAD_REQUEST)

    
    

