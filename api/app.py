from fastapi import FastAPI

from api.routers import api_router

app = FastAPI(title="Api Crossfit")

app.include_router(api_router)
