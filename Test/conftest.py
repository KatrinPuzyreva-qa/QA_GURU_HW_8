import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080