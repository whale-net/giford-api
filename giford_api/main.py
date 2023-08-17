from fastapi import FastAPI

from giford_api.routers import basic

app = FastAPI()



app.include_router(basic.router)

@app.get("/")
async def root():
    return "this is the root"