### A script to mock up API calls to the post endpoint
import requests
import numpy as np
from emnist.api import fast

url = "http://127.0.0.1:8000/array_shape"

test_arr = np.array([[2, 2, 2], [1, 1, 1]])

response = requests.post(url, data={"input": test_arr})

print(response.json)
