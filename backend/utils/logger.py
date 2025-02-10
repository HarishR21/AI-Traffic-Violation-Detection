import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_violation(vehicle_number, violation_type):
    logger.info(f"Violation detected: {violation_type} - {vehicle_number}")
