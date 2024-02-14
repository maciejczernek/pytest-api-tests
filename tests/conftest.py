import pytest
import sys
import http
import allure

from utilities.file_op import create_report_folder, copy_allure_history, \
    generate_report, create_response_log_folder
from http.client import HTTPConnection

RESULTS_PATH = "../test_results/allure-results/logs"


@pytest.fixture(scope="function", autouse=True)
def activate_logging(request):
    test_name = request.node.name
    http.client.HTTPConnection.debuglevel = 1
    stdout_origin = sys.stdout
    sys.stdout = open(f"{RESULTS_PATH}/{test_name}.txt", "w")
    yield
    sys.stdout.close()
    sys.stdout = stdout_origin
    allure.attach.file(f"{RESULTS_PATH}/{test_name}.txt", name="LOG")


@pytest.fixture(scope="session", autouse=True)
def create_log_folder():
    create_response_log_folder()


def pytest_sessionfinish():
    create_report_folder()
    copy_allure_history()
    generate_report()
