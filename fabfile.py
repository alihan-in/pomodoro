from fabric import task

@task
def run_app(c, env_file=".local.env"):
    """
    Запускает приложение с указанным env-файлом.
    По умолчанию использует .prod.env
    """
    c.run(f"poetry run uvicorn main:app --host 127.0.0.1 --port 8000 --reload --env-file {env_file}")

@task
def install_dependency(c, library):
    c.run(f"poetry add {library}")

