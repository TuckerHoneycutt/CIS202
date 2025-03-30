from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import time

app = FastAPI()

class RequestModel(BaseModel):
    input_number: int

@app.get("/")
def read_root():
    return {"message":"FastAPI Server is Running"}

@app.post("/process")
def process_data(data: RequestModel):
    """Simulates complex logic with a combination of data processing."""
    time.sleep(2)
    processed_value = (data.input_number ** 2) + random.randint(1, 100)
    if processed_value % 2 == 0:
        raise HTTPException(status_code=400, detail="Process resulted in an even number, which is not allowed.")
    return {"original":data.input_number, "processed": processed_value}
