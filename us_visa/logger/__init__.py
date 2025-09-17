import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.DEBUG,
)





