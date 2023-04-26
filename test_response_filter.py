import unittest
from response_filter import filter_response

class TestFilterResponse(unittest.TestCase):

    def test_generate_response_valid_input(self):
        messages = [{"role": "system", "content": "TestFixture: This is a valid input message."}]
        self.assertEqual(generate_response(messages), messages)

    def test_generate_response_invalid_input(self):
        messages = [{"role": "user", "content": "TestFixture: This message contains a prohibited keyword: [FILTERED]"}]
        filtered_messages = [{"role": "user", "content": "TestFixture: This message contains a prohibited keyword: [FILTERED]"}]
        self.assertNotEqual(generate_response(messages), filtered_messages)

    def test_generate_response_empty_input(self):
        messages = [{"role": "system", "content": ""}]
        self.assertEqual(generate_response(messages), messages)

    def test_generate_response_valid_and_invalid_input(self):
        messages = [{"role": "user", "content": "TestFixture: This is a valid input message. But this part contains a prohibited keyword: [FILTERED]"}]
        filtered_messages = [{"role": "user", "content": "TestFixture: This is a valid input message. But this part contains a prohibited keyword: [FILTERED]"}]
        self.assertNotEqual(generate_response(messages), filtered_messages)

if __name__ == '__main__':
    unittest.main()