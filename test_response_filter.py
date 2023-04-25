import unittest
from response_filter import filter_response

class TestFilterResponse(unittest.TestCase):

    def test_filter_response_valid_input(self):
        response = "This is a valid response."
        self.assertEqual(filter_response(response), response)

    def test_filter_response_invalid_input(self):
        response = "This response contains a prohibited keyword: [FILTERED]"
        filtered_response = "This response contains a prohibited keyword: [FILTERED]"
        self.assertNotEqual(filter_response(response), filtered_response)

    def test_filter_response_empty_input(self):
        response = ""
        self.assertEqual(filter_response(response), response)

    def test_filter_response_valid_and_invalid_input(self):
        response = "This is a valid response. But this part contains a prohibited keyword: [FILTERED]"
        filtered_response = "This is a valid response. But this part contains a prohibited keyword: [FILTERED]"
        self.assertNotEqual(filter_response(response), filtered_response)

if __name__ == '__main__':
    unittest.main()