from fastapi import FastAPI

app = FastAPI()

def calculate_factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * calculate_factorial(number - 1)

@app.get("/factorial/{number_input}")
async def calculate_factorial_endpoint(number_input: int):
    factorial_result = calculate_factorial(number_input)
    return {"number": number_input, "factorial": factorial_result}
  
   
