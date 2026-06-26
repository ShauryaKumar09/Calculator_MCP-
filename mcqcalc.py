from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP
from requests import get


mcp = FastMCP("mcp_server", stateless_http=True, host="0.0.0.0", port=8000)

@mcp.tool()
def calculator (expression: str) -> str:
    """Evaluate a mathematical expression and return the result."""
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    
@mcp.prompt()
def prompt():
    """Prompt template for the calculator tool."""
    return """
    You are a helpful assistant that can evaluate mathematical expressions.

    You can use the following tool to evaluate expressions:
    - calculator: Evaluate a mathematical expression and return the result.

    If the user asks a question that is not related to mathematics, you should say "I'm sorry, I can only answer questions about mathematics."

    You may try multiple tool calls to answer the user's question.

    You may also ask clarifying questions to the user to better understand their question.
    """

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
