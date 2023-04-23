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
BOT_PERSONALITY = "friendly and helpful"
NUM_MESSAGES_IN_PROMPT = 5
```

Update the `BOT_PERSONALITY` variable with a description that suits your desired bot personality. Modify the `NUM_MESSAGES_IN_PROMPT` variable to change the number of recent messages used to generate the bot's response.

Once the changes are made, restart the bot to apply the new settings.