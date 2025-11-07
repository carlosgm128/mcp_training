from fastmcp import FastMCP

mcp = FastMCP(name = "calculator_app")


@mcp.tool()
def add (a: float, b: float) -> float:
    """Returns the sum of two numbers.
        args:
            a (float): The first number.
            b (float): The second number.
        returns:
            float: The sum of the two numbers.
    """
    return a + b

@mcp.tool()
def multiply (a: float, b: float) -> float:
    """Returns the product of two numbers.
        args:
            a (float): The first number.
            b (float): The second number.
        returns:
            float: The product of the two numbers.
    """
    return a * b


@mcp.tool()
def subtract (a: float, b: float) -> float:
    """Returns the difference of two numbers.
        args:
            a (float): The first number.
            b (float): The second number.
        returns:
            float: The difference of the two numbers.
    """
    return a - b


@mcp.tool()
def divide (a: float, b: float) -> float:
    """Returns the quotient of two numbers.
        args:
            a (float): The first number.
            b (float): The second number.
        returns:
            float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def save_result (operation: str, result: float) -> str:
    """Saves the result of an operation to a text file.
        args:
            operation (str): The operation performed.
            result (float): The result of the operation.
        returns:
            str: Confirmation message.
    """
    with open("calculation_results.txt", "a") as file:
        file.write(f"{operation}: {result}\n")
    return "Result saved successfully."


@mcp.tool()
def read_file (filename: str) -> str:
    """Reads the contents of a text file.
        args:
            filename (str): The name of the file to read.
        returns:
            str: The contents of the file.
    """
    with open(filename, "r") as file:
        contents = file.read()
    return contents

if __name__ == "__main__":
    mcp.run()