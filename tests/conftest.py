import pytest
import sys
import http
import allure

from http.client import HTTPConnection
from .config import AllureConfig


@pytest.fixture(scope="function", autouse=True)
def activate_logging(request):
    allure_config = AllureConfig()
    test_name = request.node.name
    http.client.HTTPConnection.debuglevel = 1
    stdout_origin = sys.stdout
    sys.stdout = open(f"{allure_config.RESPONSE_LOGS}/{test_name}.txt", "w")
    yield
    sys.stdout.close()
    sys.stdout = stdout_origin
    allure.attach.file(
        source=f"{allure_config.RESPONSE_LOGS}/{test_name}.txt",
        name="LOG"
    )


@pytest.fixture(scope="session", autouse=True)
def create_log_folder():
    allure_config = AllureConfig()
    allure_config.create_response_log_folder()


def pytest_sessionfinish():
    allure_config = AllureConfig()
    allure_config.create_report_folder()
    allure_config.copy_allure_history()
    allure_config.generate_report()
