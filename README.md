#FastAPI App Documentation

This documentation provides an overview of the Interview Question program and guidelines on how to use it.

## Installation
1. Clone the repository:
 git clone <repository-url>
2. Cd Interview-Question
  
 Install dependencies
  pip install FastAPI
  pip install uvicorn





## Endpoint `/factorial/{number-input}`

This endpoint calculates the factorial of a given number.

### Functionality

Given an input number, the endpoint calculates the factorial of that number.

### Allowed Inputs

The input number must be a positive integer.




## Endpoint `/whoami`

This endpoint returns the user's IP address and the current UTC time.

### Functionality

The endpoint retrieves the user's IP address and the current UTC time.




3. Run the web service using uvicorn:
   uvicorn main:app --host 0.0.0.0 --port 8000









