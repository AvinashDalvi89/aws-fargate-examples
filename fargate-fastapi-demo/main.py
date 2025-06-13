
from fastapi import FastAPI
import time
import random
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

@app.get("/")
def read_root():
    logger.info("Healthy root endpoint hit")
    return {"message": "Hello from FastAPI on Fargate!"}

@app.get("/error")
def trigger_error():
    logger.error("Something went wrong!")
    raise Exception("Simulated server error")

@app.get("/slow")
def slow_response():
    delay = random.randint(3, 6)
    logger.warning(f"Delaying response by {delay} seconds")
    time.sleep(delay)
    return {"message": f"Response delayed by {delay} seconds"}
