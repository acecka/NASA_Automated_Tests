import unittest


def full_test_run():
    try:
        loader = unittest.TestLoader()
        tests = loader.discover(start_dir='Tests', pattern='*test.py')
        testrunner = unittest.TextTestRunner(verbosity=2)
        result = testrunner.run(tests)
    except Exception as e:
        print(f"An error occurred while running tests: {e}")


# Call the function to run all tests
full_test_run()
