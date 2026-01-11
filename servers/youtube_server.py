import logging
from core.server_factory import create_mcp_server
from tools.registry import TOOL_GROUPS

logger = logging.getLogger(__name__)

logger.info("Initializing youtube_mcp server")
youtube_mcp = create_mcp_server(
    name="youtube-mcp",
    tools=TOOL_GROUPS["youtube"]
)
