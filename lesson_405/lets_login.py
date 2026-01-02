# import logging

# logging.basicConfig(
#     filename='example.log',
#     level=logging.ERROR,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding="utf8")
# # Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# logging.debug('Це повідомлення рівня DEBUG')
# logging.info('Це повідомлення рівня INFO')
# logging.warning('Це повідомлення рівня WARNING')
# logging.error('Це повідомлення рівня ERROR')
# logging.critical('Це повідомлення рівня CRITICAL')
import sys
from pathlib import Path

project_dir = Path(__file__).parent.parent
sys.path.append(str(project_dir))

from logme.logger import logger as log

log.info("hello")