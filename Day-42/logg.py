# Here I showing Built-In LoggIng moduels


import logging
import logging.config

logging.config.fileConfig('Demo.conf')

file_handler = logging.FileHandler('Demo.log')

log = logging.getLogger('simpleExample')
log.setLevel(logging.DEBUG)
log.addHandler(file_handler)

log.debug("Debug!! fix you appliction risk too high")
log.critical("Critical!! appliction health level too high")
log.error("Error!! appliction not responding")
log.warning("Warning! appliction level too high")
log.info("Info!! appliction checker")