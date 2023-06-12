# from dotenv import dotenv_values
from fastapi import FastAPI
from src.database import database

# config = dotenv_values(".env")

app = FastAPI()

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
