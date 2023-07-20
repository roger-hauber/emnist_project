from fastapi import FastAPI

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def index():
    return {"ok": True}

@app.post("/array_shape")
async def return_arr_shape(arr):
    resp_dict = {"shape": arr.shape}
    return resp_dict
