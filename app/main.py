from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/myip")
def get_my_ip(request: Request):
    return {"client_ip": request.client.host}

@app.get("/")
def read_root():
    return {"msg": "Hello!", "v": "0.1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
