from fastapi import FastAPI
from datetime import datetime
from starlette.requests import Request

app = FastAPI()

def get_client_ip(request: Request) -> str:
    return request.client.host

@app.get("/whoami")
async def whoami(request: Request):
    client_ip = get_client_ip(request)
    current_time = datetime.utcnow().isoformat()
    return {"client": client_ip, "time": current_time}