### A script to mock up API calls to the post endpoint
import requests
import numpy as np
from emnist.api import fast

url = "http://127.0.0.1:8000/array_shape"

test_arr = np.array([[2, 2, 2], [1, 1, 1]])

payload = {
    "dim_0": test_arr.shape[0],
    "dim_1": test_arr.shape[1]
    }

response = requests.post(url, params=payload)

print(response.json)
