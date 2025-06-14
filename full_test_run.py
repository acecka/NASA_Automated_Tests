# import unittest
#
#
# def full_test_run():
#     try:
#         loader = unittest.TestLoader()
#         tests = loader.discover(start_dir='Tests', pattern='*test.py')
#         testrunner = unittest.TextTestRunner(verbosity=4)
#         result = testrunner.run(tests)
#     except Exception as e:
#         print(f"An error occurred while running tests: {e}")
#
#
# # Call the function to run all tests
# full_test_run()

import unittest
from datetime import datetime
import HTMLTestRunner
import os

# Creating a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Path to reports folder
reports_dir = 'test_reports'
os.makedirs(reports_dir, exist_ok=True)

# Creating a loader and automatically searching for tests in the test_cases folder
loader = unittest.TestLoader()
tests = loader.discover(start_dir='Tests', pattern='*test.py')

# Running tests with HTML report generation
runner = HTMLTestRunner.HTMLTestRunner(
    output=reports_dir,
    report_name=f"TestReport_{timestamp}",
    verbosity=5
)

runner.run(tests)
