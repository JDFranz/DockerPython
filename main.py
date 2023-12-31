import uvicorn
import os
from fastapi import Depends, FastAPI
import numpy as np


app = FastAPI()


@app.get("/")
def testSSL():
    # Create a NumPy array with some dummy data
    dummy_array = np.array([[1, 2, 3], [4, 5, 6]])

    # Convert the array to a string
    result_string = str(dummy_array)

    return result_string + "this was from numpy"


if __name__ == "__main__":
    if os.path.isfile("./certificates/SSL/KEY.key") and os.path.isfile(
        "./certificates/SSL/CERT.cer"
    ):
        print("https://localhost:443/docs")
        print("https://localhost:8099/docs")
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8099,
            reload=True,
            ssl_keyfile="./certificates/SSL/KEY.key",
            ssl_certfile="./certificates/SSL/CERT.cer",
        )
        # uvicorn.run('main:app', host='0.0.0.0' ,port=8099 ,reload = True )
    else:
        print("http://localhost:8099/docs")
        uvicorn.run("main:app", host="0.0.0.0", port=8099, reload=True)
