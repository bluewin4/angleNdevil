import unittest
from unittest.mock import patch
from discord_bot import DiscordBot, generate_response

class TestDiscordBot(unittest.TestCase):

    def setUp(self):
        self.bot = DiscordBot()

    def test_generate_response_with_chat_model(self):
        with patch('openai.api_call') as mock_api_call:
            mock_api_call.return_value = {'choices': [{'text': 'Test response.'}]}
            response = generate_response(prompt="Test prompt.", model="gpt-4-chat")
            self.assertEqual(response, 'Test response.')

    def test_generate_response_with_non_chat_model(self):
        with patch('openai.api_call') as mock_api_call:
            mock_api_call.return_value = {'choices': [{'text': 'Test response.'}]}
            response = generate_response(prompt="Test prompt.", model="gpt-4")
            self.assertEqual(response, 'Test response.')

if __name__ == '__main__':
    unittest.main()