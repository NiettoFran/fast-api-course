from fastapi import FastAPI

app = FastAPI(title="Fist App")


@app.get("/")
def home():
    return {
        "message": "Welcome to my first app developed with FastAPI. Author: Francisco Nietto"
    }
