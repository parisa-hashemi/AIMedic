from fastapi import FastAPI
from datetime import datetime
from starlette.requests import Request

app = FastAPI()

def calculate_factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * calculate_factorial(number - 1)

@app.get("/factorial/{number_input}")
async def calculate_factorial_endpoint(number_input: int):
    factorial_result = calculate_factorial(number_input)
    return {"number": number_input, "factorial": factorial_result}

def get_client_ip(request: Request) -> str:
    return request.client.host

@app.get("/whoami")
async def whoami(request: Request):
    client_ip = get_client_ip(request)
    current_time = datetime.utcnow().isoformat()
    return {"client": client_ip, "time": current_time}




  
   
