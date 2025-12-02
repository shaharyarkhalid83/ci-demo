# tests/test_version.py

from app.version import APP_VERSION, APP_MESSAGE

def test_version_not_empty():
    assert isinstance(APP_VERSION, str)
    assert len(APP_VERSION) > 0

def test_message_not_empty():
    assert isinstance(APP_MESSAGE, str)
    assert len(APP_MESSAGE) > 0
