
.. image:: https://img.shields.io/pypi/v/logger-color.svg
   :target: https://pypi.python.org/pypi/logger-color
.. image:: https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg
   :target: https://pypi.python.org/pypi/logger-color

logger-color
============

Color the log message headers and add more logging levels for diagnostics: DIAG_INFO, DIAG_WARNING.

============== ===== ===========
Level          Int   Color
============== ===== ===========
DEBUG          10    gray
INFO           20    green
WARNING        30    yellow
ERROR          40    red
CRITICAL       50    bold red
DIAG_INFO      21    blue
DIAG_WARNING   31    purple
============== ===== ===========

.. image:: https://github.com/vladimirs-git/logger-color/blob/main/docs/img/message_colors.png
   :alt: Message colors


Requirements
------------

Python >=3.8,<3.12


Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install logger-color

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/logger-color


start_logging()
---------------
**start_logging(filename, mode, level, level_file, color, debug)** - Start logging
with the specified parameters


Parameters
----------

=========== ======= ======= ============================================================================================
Parameter   Type    Default Description
=========== ======= ======= ============================================================================================
filename    *str*           Writes messages to this file. By default, logging only to the terminal
mode        *str*   "w"     "w" - Writes to file (default), "a" - Appends to file
level       *str*   INFO    Logging level for the terminal: "DEBUG", "INFO" (default), "WARNING", "ERROR", "CRITICAL", "DIAG_INFO", "DIAG_WARNING"
level_file  *str*   level   Logging level for the file. By default, the same as `level` parameter
color       *bool*  True    True  - Prints a colored message to the terminal (default), False - Prints a monochrome message to the terminal
debug       *bool*  False   True  - Sets logging level to DEBUG (rewrites `level` parameter), works the same as level="DEBUG". False - Gets logging level from `level` parameter (default)
=========== ======= ======= ============================================================================================


debug()
-------
**debug(args, kwargs)** - Log a message with severity "DEBUG"


diag_info()
-----------
**diag_info(msg, args, kwargs)** - Log diagnostic message with severity "INFO"


diag_warning()
--------------
**diag_warning(msg, args, kwargs)** - Log diagnostic message with severity "WARNING"


info()
------
**info(args, kwargs)** - Log a message with severity "INFO"


warning()
---------
**warning(args, kwargs)** - Log a message with severity "WARNING"


error()
-------
**error(args, kwargs)** - Log a message with severity "ERROR"


critical()
----------
**warning(args, kwargs)** - Log a message with severity "CRITICAL"


**Example**

.. code:: python

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
