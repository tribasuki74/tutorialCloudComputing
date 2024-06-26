from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def root():
    return {"message": "Hello World from /hello"}

@app.get("/get")
async def root():
    return {"message": "Hello get"}