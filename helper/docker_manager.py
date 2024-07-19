import docker
from docker.types import Resources


client = docker.from_env()

def create_container(code: str, cpu: int, memory: float, storage: float, gpu: int):
    resource_constraints = {
        'cpus': cpu,
        'mem_limit': f'{memory}g',
        'device_requests': [
            {
                'Driver': 'nvidia',
                'Count': gpu,
                'Capabilities': [['gpu']]
            }
        ] if gpu > 0 else None
    }

    container = client.containers.run(
        "amd64/python:3",
        command=f"python -c '{code}'",
        detach=True,
        resources = Resources(**resource_constraints),
        volumes={'/tmp': {'bind': '/mnt', 'mode': 'rw'}}
    )
    return container

if __name__=="__main__":
    code = "print(\"Hello world!\")";
    container = create_container(code, 2, 2, 1, 0)
    container.wait()
    logs = container.logs().decode('utf-8')
    container.remove()
