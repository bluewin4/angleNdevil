import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY
bot = commands.Bot(command_prefix='!')

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
    try:
        conversation_history = await get_conversation(ctx, num_messages)
        prompt = f'As an AI language model with a {selected_personality} personality, embody the characteristics and traits of this personality while responding to the following conversation:\n\n{conversation_history}\nHow would a {selected_personality}-like AI respond?'
        response = generate_response(prompt)
        await ctx.send(response)
    except Exception as e:
        print(f'Error: {e}')
        await ctx.send('An error occurred while generating a response. Please try again.')

async def get_conversation(ctx, num_messages: int):
    messages = await ctx.channel.history(limit=num_messages).flatten()
    conversation_history = ''
    for message in reversed(messages):
        conversation_history += f'{message.author}: {message.content}\n'
    return conversation_history

def generate_response(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()

bot.run(TOKEN)