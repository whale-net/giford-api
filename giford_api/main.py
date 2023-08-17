from fastapi import FastAPI

# using relative because mypy seems to like that
from .routers import basic

app = FastAPI()



app.include_router(basic.router)

@app.get("/")
async def root() -> str:
    return "this is the root"