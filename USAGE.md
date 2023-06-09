## Setting Up and Using the Discord Bot

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications) and add it to your `.env` file:
   ```
   DISCORD_BOT_TOKEN=<your_discord_bot_token>
   ```
5. Obtain an OpenAI API key by signing up for an account at [OpenAI](https://beta.openai.com/signup/) and add it to your `.env` file:
   ```
   OPENAI_API_KEY=<your_openai_api_key>
   ```
6. Run the bot:
   ```
   python discord_bot.py
   ```
7. [Invite the Discord bot to your server](https://discordpy.readthedocs.io/en/latest/discord.html) and send messages in a text channel to interact with it.

### Configuring the Bot's Personality and Context Length

You can configure the bot's personality and the number of messages to include in the chat context by modifying the following variables in `discord_bot.py`:

```python
BOT_PERSONALITY_DESCRIPTION = "friendly and helpful"
CONTEXT_MESSAGE_LIMIT = 5

Update the `BOT_PERSONALITY_DESCRIPTION` variable with a description that suits your desired bot personality. Modify the `CONTEXT_MESSAGE_LIMIT` variable to change the number of recent messages used to generate the bot's response.

### The !coach Command

The `!coach` command now utilizes the `v1/chat/completions` endpoint for chat models, enhancing the quality and creativity of the bot's responses. To use the `!coach` command, prefix your message with `!coach`, and the bot will generate a response based on the chat models and the provided conversation history as an array of messages.

To further customize the bot's responses, modify the `response_filter.py` file and update the filtering and creativity functions as needed. After making changes, restart the bot to implement the new settings.