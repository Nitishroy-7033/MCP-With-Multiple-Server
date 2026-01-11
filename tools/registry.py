import logging
from tools.school.student import get_student, get_student_by_name
from tools.school.list_students import list_students
from tools.youtube.analytics import get_channel_analytics
from tools.youtube.upload import upload_video

logger = logging.getLogger(__name__)

logger.info("Registering tools in TOOL_GROUPS")

TOOL_GROUPS = {
    "school": [get_student, get_student_by_name, list_students],
    "youtube": [get_channel_analytics, upload_video],
}

# Combine all tools for the "all" group
TOOL_GROUPS["all"] = [tool for group in TOOL_GROUPS.values() for tool in group]

logger.info(f"Registered tool groups: {list(TOOL_GROUPS.keys())}")
