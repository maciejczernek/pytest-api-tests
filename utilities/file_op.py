import os
import shutil

RESULTS_PATH = "../test_results"


def copy_allure_history():
    history_path = os.path.join(RESULTS_PATH, r"allure-report/history")
    target_path = os.path.join(RESULTS_PATH, r"allure-results/history")

    if not os.path.isdir(history_path):
        return

    if os.path.isdir(target_path):
        return

    shutil.copytree(history_path, target_path, dirs_exist_ok=True)


def generate_report():
    os.chdir(RESULTS_PATH)
    os.system("allure generate --clean")


def create_report_folder():
    path = os.path.join(RESULTS_PATH, r"allure-report")
    if not os.path.isdir(path):
        os.mkdir(path)


def create_response_log_folder():
    path = os.path.join(RESULTS_PATH, r"allure-results/logs")
    if not os.path.isdir(path):
        os.mkdir(path)
