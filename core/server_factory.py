import logging
from mcp.server.fastmcp import FastMCP

def create_mcp_server(name: str, tools: list) -> FastMCP:
    try:
        server = FastMCP(name=name)
        for tool_fn in tools:
            server.add_tool(tool_fn)  

        return server
    except Exception as e:
        raise
