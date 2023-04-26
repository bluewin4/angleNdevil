import os
import discord
import openai
from discord.ext import commands
from response_filter import filter_response
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY
bot = commands.Bot(command_prefix='!')
selected_engine = "text-davinci-003"

@bot.command(name='select_engine', help='Select the language model engine to use. Examples: gpt-4, gpt-4-0314, gpt-4-32k, gpt-4-32k-0314, gpt-3.5-turbo, gpt-3.5-turbo-0301')
async def select_engine(ctx, engine: str):
    global selected_engine
    selected_engine = engine
    await ctx.send(f'Language model engine set to: {selected_engine}')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='select_personality', help='Manually select a personality for the AI coach.')
async def select_personality(ctx, personality: str):
    global selected_personality
    selected_personality = personality
    await ctx.send(f'Personality set to: {selected_personality}')

@bot.command(name='coach', help='Generates a response based on the specified personality and conversation context.')
async def coach(ctx, num_messages: int = 10):
    if num_messages <= 0:
        await ctx.send('Number of messages must be greater than 0.')
        return

    try:
        conversation_history = await get_conversation(ctx, num_messages)
        if not conversation_history:
            await ctx.send('No conversation history found.')
            return

        prompt = f'As an AI language model with a {selected_personality} personality, embody the characteristics and traits of this personality while responding to the following conversation:\n\n{conversation_history}\nHow would a {selected_personality}-like AI respond?'
        response = generate_response(prompt, conversation_history)
        filtered_response = filter_response(response)

        if not filtered_response:
            await ctx.send('Unable to generate a suitable response. Please try again.')
        else:
            await ctx.send(filtered_response)
    except Exception as e:
        print(f'Error in `coach` command: {e}')
        await ctx.send('An error occurred while generating a response. Please try again.')

async def get_conversation(ctx, num_messages: int):
    messages = await ctx.channel.history(limit=num_messages).flatten()
    conversation_history = [{"role": "system" if message.author.bot else "user", "content": message.content} for message in reversed(messages)]
    return conversation_history

def generate_response(prompt, messages):
    try:
        response = openai.Completion.create(
            engine=selected_engine,
            prompt=prompt,
            max_tokens=150,
            temperature=0.8,
            n=1
        )
        generated_text = response["choices"][0]["text"].strip()
        return generated_text
    except Exception as e:
        print(f'Error: {e}')
        raise

bot.run(TOKEN)
