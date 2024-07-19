import docker

client = docker.from_env()
container = client.containers.run("ubuntu", "echo hello world", detach=True)
container.wait()
logs = container.logs().decode('utf-8')
print(logs)
container.remove()
