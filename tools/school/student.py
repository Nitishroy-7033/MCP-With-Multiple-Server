import logging

logger = logging.getLogger(__name__)

def get_student(student_id: str) -> dict:
    """
    Get student details by ID
    """
    logger.info(f"Executing get_student (by ID) with student_id: {student_id}")
    try:
        # Simulate data retrieval
        student_data = {
            "id": student_id,
            "name": "John Doe",
            "class": "10A"
        }
        logger.debug(f"Successfully retrieved student data: {student_data}")
        return student_data
    except Exception as e:
        logger.error(f"Error in get_student for ID {student_id}: {str(e)}")
        raise

def get_student_by_name(name: str) -> dict:
    """
    Get student details by name
    """
    logger.info(f"Executing get_student_by_name with name: {name}")
    try:
        # Simulate data retrieval
        student_data = {
            "id": "1",
            "name": name,
            "class": "10A"
        }
        logger.debug(f"Successfully retrieved student data: {student_data}")
        return student_data
    except Exception as e:
        logger.error(f"Error in get_student_by_name for name {name}: {str(e)}")
        raise
