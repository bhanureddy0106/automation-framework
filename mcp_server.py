from mcp.server.fastmcp import FastMCP
import subprocess
import sys

mcp = FastMCP("AutomationFramework")

print("MCP Server Started", file=sys.stderr)

# DIRECT EXECUTION
result = subprocess.run(
    ["pytest", "tests"],
    text=True,
    capture_output=True
)

print(result.stdout)

@mcp.tool()
def run_pytest():
    return result.stdout

if __name__ == "__main__":
    mcp.run(transport="stdio")