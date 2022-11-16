from invoke import task
from invoke import run


@task
def build(cmd):
    cmd.run("docker compose --env-file app/.env build")
    print("Build done...")


@task
def up(cmd):
    cmd.run("docker compose --env-file app/.env up -d")
    print("Running services...")


@task
def update_deps(cmd):
    cmd.run("rm -f app/requirements.txt")
    cmd.run("pip freeze > app/requirements.txt")
    print("Updated app/requirements.txt")
