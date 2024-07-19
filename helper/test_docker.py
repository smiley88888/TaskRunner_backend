import docker

client = docker.from_env()
container = client.containers.run("ubuntu", "echo hello world")
container.wait()
logs = container.logs().decode('utf-8')
container.remove()
