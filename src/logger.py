import logging
from datetime import datetime
import os 

# 🔹 Ensure 'logs' directory exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)  # ✅ Create the 'logs' folder, not a file

# 🔹 Define log file name and path
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # ✅ Use '.log', not '.logs'
log_file_path = os.path.join(log_dir, log_file)

# 🔹 Set up logging configuration
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] ** %(lineno)d ** %(name)s ** %(levelname)s ** %(message)s",  # ✅ Fixed 'lineno'
    level=logging.INFO,
)
