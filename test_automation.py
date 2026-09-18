import unittest

import automation


class TestAutomation(unittest.TestCase):

    def test_clean_sales_removes_invalid_records(self):
        records = [
            {
                "customer": "Ali",
                "product": "Mouse",
                "amount": 1000
            },
            {
                "customer": "",
                "product": "Keyboard",
                "amount": 2000
            },
            {
                "customer": "Sara",
                "product": "Monitor",
                "amount": -10
            }
        ]

        result = automation.clean_sales(records)

        self.assertEqual(len(result), 1)

    def test_report_total(self):
        records = [
            {
                "customer": "Ali",
                "product": "Mouse",
                "amount": 1000
            },
            {
                "customer": "Sara",
                "product": "Keyboard",
                "amount": 2000
            }
        ]

        total = automation.create_report(records)

        self.assertEqual(total, 3000)


if __name__ == "__main__":
    unittest.main()