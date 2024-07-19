from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
import logging
from helper.docker_manager import create_container


logger = logging.getLogger(__name__)


async def taskrunner(request: Request):
    try:
        incoming_data = await request.json()
        logger.info("incoming_data %s", incoming_data)

        task_type = incoming_data["task_type"]
        code = incoming_data["code"]
        cpu = incoming_data["resources"]["cpu"]
        gpu = incoming_data["resources"]["gpu"]
        ram = incoming_data["resources"]["ram"]
        store = incoming_data["resourcs"]["storage"]

    except Exception as e:
        logger.error(str(e))
        return JSONResponse(content={"message":"failed", "result":""}, status_code=status.HTTP_400_BAD_REQUEST)
    
    try:
        container = create_container(code, cpu, ram, store, gpu)
        container.wait()
        logs = container.logs().decode('utf-8')
        container.remove()
        return JSONResponse(content={"message":"success", "result":logs}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(content={"message":"failed", "result":""}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

