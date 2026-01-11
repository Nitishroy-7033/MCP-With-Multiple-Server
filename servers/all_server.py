import logging
from core.server_factory import create_mcp_server
from tools.registry import TOOL_GROUPS

logger = logging.getLogger(__name__)

logger.info("Initializing all_mcp server")
all_mcp = create_mcp_server(
    name="all-mcp",
    tools=TOOL_GROUPS["all"]
)
