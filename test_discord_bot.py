import unittest
from unittest.mock import patch
from discord_bot import DiscordBot, generate_response

class TestDiscordBot(unittest.TestCase):

    def setUp(self):
        self.bot = DiscordBot()

    def test_generate_response_with_chat_model(self):
        with patch('openai.api_call') as mock_api_call:
            mock_api_call.return_value = {'choices': [{'text': 'Test response.'}]}
            response = generate_response(prompt="Test prompt.", model="gpt-4-chat", messages=[{'role': 'system', 'content': 'Starting a conversation.'}])
            self.assertEqual(response, 'Test response.')
            mock_api_call.assert_called_once_with(
                'v1/engines/gpt-4-chat/completions', data={'messages': [{'role': 'system', 'content': 'Starting a conversation.'}], 'model': 'gpt-4-chat', 'prompt': 'Test prompt.'}
            )

    def test_generate_response_with_non_chat_model(self):
        with patch('openai.api_call') as mock_api_call:
            mock_api_call.return_value = {'choices': [{'text': 'Test response.'}]}
            response = generate_response(prompt="Test prompt.", model="gpt-4", messages=[])
            self.assertEqual(response, 'Test response.')
            mock_api_call.assert_called_once_with(
                'v1/engines/gpt-4/completions', data={'messages': [], 'model': 'gpt-4', 'prompt': 'Test prompt.'}
            )
                'v1/engines/gpt-4/completions', data={'messages': [], 'model': 'gpt-4', 'prompt': 'Test prompt.'}
            )
def test_coach_command_with_valid_input(self):
    with patch('discord_bot.generate_response') as mock_generate_response:
        mock_generate_response.return_value = 'Coaching advice'
        response = self.bot.process_command('bluerune#7459: !coach 1')
        self.assertEqual(response, 'Coaching advice')
        mock_generate_response.assert_called_once_with(prompt='1', model='gpt-4-chat', messages=[])

def test_coach_command_with_invalid_input(self):
    with patch('discord_bot.generate_response') as mock_generate_response:
        response = self.bot.process_command('bluerune#7459: !coach invalid')
        self.assertEqual(response, 'Invalid input for !coach command. Please enter a number.')
        mock_generate_response.assert_not_called()

if __name__ == '__main__':
    unittest.main()