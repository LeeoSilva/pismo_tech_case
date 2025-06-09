from src.settings import settings


def build_connection_string() -> str:
    user: str = settings().db_user
    password: str = settings().db_password
    host: str = settings().db_host
    port: str = settings().db_port
    db_name: str = settings().db_name

    driver: str = "postgresql+psycopg2"

    return f"{driver}://{user}:{password}@{host}:{port}/{db_name}"
