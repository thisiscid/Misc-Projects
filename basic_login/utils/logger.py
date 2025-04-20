import time
def log(log_item, category="INFO"):
    """Function to log messages to a file with a timestamp and category,
    which can be invoked by other modules.
    Input:
    log_item: str - The message to be logged.
    category: str - Category of the log message (default is "INFO").
    """
    with open("login.log", "a") as file: # Open the log file in append mode
        file.write(f"{time.asctime()} - {category} - {log_item} \n") # Write the log message with a timestamp