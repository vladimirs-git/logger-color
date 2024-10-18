"""Tests logger_color"""

import pytest

from logger_color import CLogger


@pytest.mark.parametrize("params, expected", [
    ({}, True),
    ({"color": None}, True),
    ({"color": True}, True),
    ({"color": False}, False),
    ({"color": 0}, False),
    ({"color": 1}, True),
])
def test__init_color(params, expected):
    """CLogger._init_color()"""
    logger = CLogger()

    actual = logger._init_color(**params)

    assert actual == expected


@pytest.mark.parametrize("params, expected", [
    ({}, 20),
    ({"debug": True}, 10),
    ({"debug": False}, 20),
    ({"debug": 0}, 20),
    ({"debug": 1}, 10),
    ({"level": None}, 20),
    ({"level": 11}, 11),
    ({"level": "debug"}, 10),
    ({"level": "info"}, 20),
    ({"level": "warning"}, 30),
    ({"level": "error"}, 40),
    ({"level": "fatal"}, 50),
    ({"level": "critical"}, 50),
    ({"level": "DEBUG"}, 10),
    ({"level": "INFO"}, 20),
    ({"level": "WARNING"}, 30),
    ({"level": "ERROR"}, 40),
    ({"level": "FATAL"}, 50),
    ({"level": "CRITICAL"}, 50),
    ({"debug": True, "level": "warning"}, 10),
    ({"debug": False, "level": "warning"}, 30),
])
def test__init_level(params, expected):
    """CLogger._init_level()"""
    logger = CLogger()

    actual = logger._init_level(**params)

    assert actual == expected


@pytest.mark.parametrize("params, expected", [
    ({}, "w"),
    ({"mode": None}, "w"),
    ({"mode": "a"}, "a"),
    ({"mode": "w"}, "w"),
    ({"mode": 0}, ValueError),
    ({"mode": "r"}, ValueError),
])
def test__init_mode(params, expected):
    """CLogger._init_mode()"""
    logger = CLogger()
    if isinstance(expected, str):
        actual = logger._init_mode(**params)
        assert actual == expected
    else:
        with pytest.raises(expected):
            logger._init_mode(**params)
