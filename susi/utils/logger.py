import sys
from loguru import logger

# Clear the current log handlers
logger.remove()

# Add a rotating file handler
# The log files will be rotated when they reach 5 MB in size
# The maximum number of log files retained is 10
# The log files are stored in the "logs" directory
logger.add(
    "logs/log.txt",
    rotation="5 MB",
    retention=10,
)

# Define the format of the log messages
# The format includes the time, log level, logger name, function name, line number, and log message
logger_format = (
    "<white>{time:YYYY-MM-DD HH:mm:ss.SSS}</white> | "
    "<level>{level}</level> | "
    "{file} | "
    "<level>{message}</level>"
)

# Add a console handler to print log messages to the standard error stream
logger.add(sys.stderr, format=logger_format)

# Define a helper function to create a logger instance with a specified name
# The logger instance has the specified name bound to it
def log(name: str) -> logger.__class__:
    return logger.bind(name=name)
