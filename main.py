import discord
from discord import app_commands
import requests
import os
from dotenv import load_dotenv


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
load_dotenv()



def get_answers(question, model): 
    headers  = {
        "Content-Type": "application/json"
    }

    payload = {
        "question": question,
        "model": "solidity",
        "master_key": os.getenv("master_key"),
    
    }
    r = requests.post("https://unamed-ai-k7ml7hype-aaravatgits-projects.vercel.app/ask", params=payload, headers=headers)
    print(r.json(), r.status_code)
    return r.json()



@tree.command(name="ping", description="Returns Pong!")
async def ping(interaction):
    await interaction.response.send_message(f"pong, {round(client.latency * 1000)}ms")


@tree.command(name="ask", description="Ask the A.I")
async def ask(interaction, question: str, model: str="solidity"):
    await interaction.response.defer()
    response = get_answers(question, model)
    await interaction.followup.send(response["answer"])



@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user.name} is Ready!")





client.run(os.getenv("token"))