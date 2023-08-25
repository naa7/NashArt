import os
import interactions
from interactions import OptionType, slash_option, slash_command, SlashContext
import NashArt
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = interactions.Client(activity="Answer Art Responses")
response_history = {}

@interactions.listen()
async def on_startup():
    print(f"Logged in as {bot.user}")

@bot.event()
async def on_ready():
    print("Im ready!")

def generate_response(prompt, author_id):
    if author_id in response_history and response_history[author_id]:
        prompt_with_history = "Previous responses: " + "\n".join(response_history[author_id]) + f"\n\nInquiry: {prompt}"

    else:
        prompt_with_history = prompt
    print(prompt_with_history)
    response = NashArt.generate_response(prompt_with_history)
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
@slash_command(name="ask", description="I can help to answer any questions")

@slash_option(name="prompt",
                           description="Enter your prompt",
                           required=True,
                           opt_type=OptionType.STRING)

async def ask(ctx: SlashContext, prompt: str):
    await ctx.defer()
    response_max_size = 1900
    author_id = ctx.author.id
    response = str(generate_response(prompt, author_id))
    if author_id not in response_history:
        response_history[author_id] = []
    response_history[author_id].append(response)
    if len(response_history[author_id]) > 5:
        response_history[author_id].pop(0)
    if len(response) <= response_max_size:
        await ctx.respond(response)
    else:
        response_chunks = response_split(response, response_max_size)
        for chunk in response_chunks:
            await ctx.respond(chunk)

###########################################
# 2) "tts-ask" command
@slash_command(name="tts-ask",
                            description="I can help to answer any questions in text-to speech")

@slash_option(name="prompt",
                           description="Enter your prompt",
                           required=True,
                           opt_type=OptionType.STRING)

async def tts_ask(ctx: SlashContext, prompt: str):
    await ctx.defer()
    response_max_size = 1900
    author_id = ctx.author.id
    response = str(generate_response(prompt, author_id))
    if author_id not in response_history:
        response_history[author_id] = []
    response_history[author_id].append(response)
    if len(response_history[author_id]) > 5:
        response_history[author_id].pop(0)
    if len(response) <= response_max_size:
        await ctx.respond(response, tts=True)
    else:
        response_chunks = response_split(response, response_max_size)
        for chunk in response_chunks:
            await ctx.respond(chunk, tts=True)


###########################################
# 3) "help" 
help_message = (
    "```Commands list:\n\n"
    "/ask - chats or answers any art questions\n"
    "/tts-ask - same as /ask + text-to-speech ability```"
)

@slash_command(name="help",
                            description="display help menu")

async def help(ctx: SlashContext):
    await ctx.respond(help_message)

keep_alive()
bot.start(TOKEN)