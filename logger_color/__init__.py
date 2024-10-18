"""logger-color"""

from logger_color.clogger import CLogger
from logger_color.functions import debug, info, warning, error, critical
from logger_color.functions import start_logging, diag_info, diag_warning

__all__ = [
    "CLogger",
    "critical",
    "debug",
    "diag_info",
    "diag_warning",
    "error",
    "info",
    "start_logging",
    "warning",
]
