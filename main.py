from fastapi import FastAPI
from handlers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


for router in routers:
    app.include_router(router)
