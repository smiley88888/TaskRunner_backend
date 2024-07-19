# TaskRunner

**Summary:**
The TaskRunner project aims to develop a Python-based API using FastAPI to manage and execute tasks dynamically. 
These tasks include executable code snippets provided by clients, which are securely executed within Docker containers. 
The system is designed to dynamically allocate resources such as CPU, GPU, RAM, and storage based on the specific needs of each task.

## Endpoints
### Execute Task
**Endpoint:** /api/taskrunner/task

**Method:** POST

**Request Body:**

The body should be a JSON object containing the following fields:
- code (string): The code snippet to be executed.
- cpu (int): The number of CPU cores to allocate to the Docker container.
- memory (float): The amount of RAM to allocate (e.g., “512m” for 512 MB).
- storage (float): The amount of storage to allocate (not directly used in Docker configuration but can be considered for volume management).
- gpu (int, optional): The GPU resources to allocate, if any.

**Example Request:**

`{
    "code": "print('Hello, world!')",
    "cpu": "1",
    "memory": "0.5",
    "storage": "1",
    "gpu": "0"
}`
