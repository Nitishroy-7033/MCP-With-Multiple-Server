import logging

logger = logging.getLogger(__name__)

def list_students() -> list[dict]:
    """
    List all students in the registry.
    """
    logger.info("Executing list_students")
    try:
        students = [
            {"id": "1", "name": "John Doe", "class": "10A"},
            {"id": "2", "name": "Jane Smith", "class": "11B"},
            {"id": "3", "name": "Bob Johnson", "class": "9C"},
        ]
        logger.debug(f"Retrieved {len(students)} students")
        return students
    except Exception as e:
        logger.error(f"Error in list_students: {str(e)}")
        raise
