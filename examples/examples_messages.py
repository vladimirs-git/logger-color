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
# 2000-12-31 23:59:59.474 DEBUG    messages.debug: debug
# 2000-12-31 23:59:59.474 INFO     messages.info: info
# 2000-12-31 23:59:59.474 WARNING  messages.warning: warning
# 2000-12-31 23:59:59.474 ERROR    messages.error: error
# 2000-12-31 23:59:59.474 CRITICAL messages.critical: critical
# 2000-12-31 23:59:59.474 DIAG_I   messages.<module>: diag_info
# 2000-12-31 23:59:59.474 DIAG_W   messages.<module>: diag_warning

# cat /var/log/test.log
# 2000-12-31 23:59:59 ERROR    error
# 2000-12-31 23:59:59 CRITICAL critical
