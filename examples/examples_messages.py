"""Examples"""

import logger_color

logger_color.start_logging(filename="/var/log/test.log", level="debug", level_file="error")
logger_color.debug("debug")
logger_color.info("info")
logger_color.warning("warning")
logger_color.error("error")
logger_color.critical("critical")
logger_color.diag_info("diag_info")
logger_color.diag_warning("diag_warning")
# 2024-10-19 11:03:25.691 DEBUG    functions.debug: debug
# 2024-10-19 11:03:25.691 INFO     functions.info: info
# 2024-10-19 11:03:25.691 WARNING  functions.warning: warning
# 2024-10-19 11:03:25.691 ERROR    functions.error: error
# 2024-10-19 11:03:25.691 CRITICAL functions.critical: critical
# 2024-10-19 11:03:25.691 DIAG_I   examples_messages.<module>: diag_info
# 2024-10-19 11:03:25.691 DIAG_W   examples_messages.<module>: diag_warning

# cat /var/log/test.log
# 2024-10-19 11:03:25 ERROR    error
# 2024-10-19 11:03:25 CRITICAL critical
