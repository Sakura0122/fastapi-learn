from fastapi import FastAPI

app = FastAPI()


@app.get("/",summary="首页")
def read_root():
    return {"Hello": "World"}
