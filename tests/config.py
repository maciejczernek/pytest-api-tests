import os

from utilities.base_file import copy_dir, create_dir


class AllureConfig:
    TEST_RESULTS = r"..\test_results"
    REPORT_FOLDER = os.path.join(TEST_RESULTS, "allure-report")
    RESULTS_FOLDER = os.path.join(TEST_RESULTS, "allure-results")
    HISTORY_PATH_REPORT = os.path.join(REPORT_FOLDER, "history")
    HISTORY_PATH_RESULTS = os.path.join(RESULTS_FOLDER, "history")
    RESPONSE_LOGS = os.path.join(TEST_RESULTS, RESULTS_FOLDER, "logs")

    def copy_allure_history(self):
        if not os.path.isdir(self.HISTORY_PATH_REPORT):
            return
        if os.path.isdir(self.HISTORY_PATH_RESULTS):
            return
        copy_dir(self.HISTORY_PATH_REPORT, self.HISTORY_PATH_RESULTS)

    def generate_report(self):
        os.chdir(self.TEST_RESULTS)
        os.system("allure generate --clean")

    def create_report_folder(self):
        create_dir(self.REPORT_FOLDER)

    def create_response_log_folder(self):
        create_dir(self.RESPONSE_LOGS)
