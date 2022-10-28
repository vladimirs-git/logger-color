"""Unittests package logger_color.py"""

import unittest

from logger_color import CLogger


class Test(unittest.TestCase):
    """Logger"""

    def test_valid__init_color(self):
        """Logger._init_color()"""
        logger = CLogger()
        for kwargs, req in [
            ({}, True),
            (dict(color=None), True),
            (dict(color=True), True),
            (dict(color=False), False),
            (dict(color=0), False),
            (dict(color=1), True),
        ]:
            result = logger._init_color(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__init_level(self):
        """Logger._init_level()"""
        logger = CLogger()
        for kwargs, req in [
            ({}, 20),
            (dict(debug=True), 10),
            (dict(debug=False), 20),
            (dict(debug=0), 20),
            (dict(debug=1), 10),
            (dict(level=None), 20),
            (dict(level=11), 11),
            (dict(level="debug"), 10),
            (dict(level="info"), 20),
            (dict(level="warning"), 30),
            (dict(level="error"), 40),
            (dict(level="fatal"), 50),
            (dict(level="critical"), 50),
            (dict(level="DEBUG"), 10),
            (dict(level="INFO"), 20),
            (dict(level="WARNING"), 30),
            (dict(level="ERROR"), 40),
            (dict(level="FATAL"), 50),
            (dict(level="CRITICAL"), 50),
            (dict(debug=True, level="warning"), 10),
            (dict(debug=False, level="warning"), 30),
        ]:
            result = logger._init_level(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__init_mode(self):
        """Logger._init_mode()"""
        logger = CLogger()
        for kwargs, req in [
            ({}, "w"),
            (dict(mode=None), "w"),
            (dict(mode="a"), "a"),
            (dict(mode="w"), "w"),
        ]:
            result = logger._init_mode(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_mode(self):
        """Logger._init_mode()"""
        logger = CLogger()
        for kwargs, error in [
            (dict(mode=0), ValueError),
            (dict(mode="r"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                logger._init_mode(**kwargs)


if __name__ == "__main__":
    unittest.main()
