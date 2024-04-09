import unittest
import HTMLTestRunner


class CustomHTMLTestRunner(HTMLTestRunner.HTMLTestRunner):
    def generate_report(self, result):
        # Your existing code to generate the report
        additional_info = "This is additional information about the test results."
        return additional_info
