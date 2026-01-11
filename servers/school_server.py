import logging
from core.server_factory import create_mcp_server
from tools.registry import TOOL_GROUPS

logger = logging.getLogger(__name__)

logger.info("Initializing school_mcp server")
school_mcp = create_mcp_server(
    name="school-mcp",
    tools=TOOL_GROUPS["school"]
)
