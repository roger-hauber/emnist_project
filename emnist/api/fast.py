from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def index():
    return {"ok": True}


class arr_shape(BaseModel):
    dim_0: int
    dim_1: int

@app.post("/array_shape")
async def return_arr_shape(shp: arr_shape):
    resp_dict = {"shape": (shp.dim_0, shp.dim_1)}
    return resp_dict
