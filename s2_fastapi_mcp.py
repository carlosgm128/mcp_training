from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

router = APIRouter()

app = FastAPI(title="My FastAPI MCP Application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the FastAPI MCP Application!"}

@app.post("/multiply")
def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

@app.post("/add")
def add_numbers(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

@app.post("/subtract")
def subtract_numbers(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result."""
    return a - b

@app.post("/divide")
def divide_numbers(a: float, b: float) -> float:
    """Divides two numbers and returns the result."""
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return a / b


# converting the FastAPI app to a format suitable for MCP
mcp = FastApiMCP(app, name="Calculator FastAPIMCP")
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)