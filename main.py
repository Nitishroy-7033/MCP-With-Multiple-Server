from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from servers.school_server import school_mcp
from servers.youtube_server import youtube_mcp
from servers.all_server import all_mcp
from core.logging_config import setup_logging

logger = setup_logging()
logger.info("Starting Multi-Server MCP Application")

app = FastAPI()

# Helper to add a redirect route for mounted servers
def add_mcp_redirects(app: FastAPI, path: str):
    @app.api_route(path, methods=["GET", "POST"], include_in_schema=False)
    @app.api_route(f"{path}/", methods=["GET", "POST"], include_in_schema=False)
    async def redirect_to_sse():
        return RedirectResponse(url=f"{path}/sse")

logger.info("Mounting School MCP server at /mcp/school")
app.mount("/mcp/school", school_mcp.sse_app())
add_mcp_redirects(app, "/mcp/school")

logger.info("Mounting YouTube MCP server at /mcp/youtube")
app.mount("/mcp/youtube", youtube_mcp.sse_app())
add_mcp_redirects(app, "/mcp/youtube")

logger.info("Mounting Combined (All) MCP server at /mcp/all")
app.mount("/mcp/all", all_mcp.sse_app())
add_mcp_redirects(app, "/mcp/all")

@app.get("/health")
async def health_check():
    """
    Check the health of the application and its components.
    """
    logger.debug("Health check requested")
    return {
        "status": "healthy",
        "services": {
            "school_mcp": "running",
            "youtube_mcp": "running",
            "all_mcp": "running"
        }
    }

@app.get("/")
async def root():
    """
    Root endpoint providing information about the available MCP servers.
    """
    return {
        "message": "Multi-Server MCP Gateway is running",
        "endpoints": {
            "school": "/mcp/school",
            "youtube": "/mcp/youtube",
            "all": "/mcp/all",
            "health": "/health"
        }
    }


