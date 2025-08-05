from fastapi import FastAPI

from app.gandalf.router import get_router


def run() -> FastAPI:
    app = FastAPI(title="Gandalf API")

    router = get_router()
    app.include_router(router)

    return app
