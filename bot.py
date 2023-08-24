import discord
import os, NashArt
import interactions
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
bot = interactions.Client(activity=discord.Game("Answer Art Responses"),
                          status=discord.Status.do_not_disturb)


@interactions.listen()
async def on_startup():
    print(f"Logged in as {bot.user}")


@bot.event()
async def on_ready():
    print("Im ready!")


def generate_response(prompt):
    response = NashArt.generate_response(prompt)
    return response

def response_split(response, response_max_length):
    response_chunks = []
    current_chunk = ""
    words = response.split(' ')
    for word in words:
        if len(current_chunk) + len(word) < response_max_length:
            current_chunk = current_chunk + word + ' '
        else:
            response_chunks.append(current_chunk.strip())
            current_chunk = word + ' '
    if current_chunk:
        response_chunks.append(current_chunk.strip())

    return response_chunks

###########################################
# 1) "ask" command
@interactions.slash_command(name="ask",
                            description="I can help to answer any questions",
                            )

@interactions.slash_option(name="prompt",
                           description="Enter your prompt",
                           required=True,
                           opt_type=interactions.OptionType.STRING)

async def ask(ctx: interactions.SlashContext, prompt: str):
    await ctx.defer()
    response_max_size = 1900
    response = generate_response(prompt)
    if len(response) <= response_max_size:
        await ctx.respond(response)
    else:
        response_chunks = response_split(response, response_max_size)
        for chunk in response_chunks:
            await ctx.respond(chunk)

###########################################
# 2) "tts-ask" command
@interactions.slash_command(name="tts-ask",
                            description="I can help to answer any questions in text-to-speech",
                            )

@interactions.slash_option(name="prompt",
                           description="Enter your prompt",
                           required=True,
                           opt_type=interactions.OptionType.STRING)

async def tts_ask(ctx: interactions.SlashContext, prompt: str):
    await ctx.defer()
    response_max_size = 1900
    response = generate_response(prompt)
    if len(response) <= response_max_size:
        await ctx.respond(response, tts=True)
    else:
        response_chunks = response_split(response, response_max_size)
        for chunk in response_chunks:
            await ctx.respond(chunk, tts=True)


###########################################
# 3) "help" command
@interactions.slash_command(name="help",
                            description="display help menu",
                            )

async def help(ctx: interactions.SlashContext):
    await ctx.respond(
        '''```Commands list:\n\n/ask - chats or answers any art quesitons\n\n/tts-ask - same as /ask + text-to-speech ability\n```'''
    )

keep_alive()
bot.start(TOKEN)