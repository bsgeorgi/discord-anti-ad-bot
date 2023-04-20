import os
import discord
from config import *
from discord.ext import commands
from violations import load_violations, save_violations
from challenge import send_challenge, is_advertising
from commands import setup as load_commands

# Load violations data
violations = load_violations(VIOLATIONS_FILE)

# Initialize the bot and load commands
bot = commands.Bot(command_prefix='!', intents=intents)
load_commands(bot)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Delete messages containing advertisements
    if is_advertising(message.content):
        await message.delete()
        user_id = str(message.author.id)
        if user_id not in violations:
            violations[user_id] = 1
        else:
            violations[user_id] += 1

        # Ban the user if they exceed the maximum violations count
        if violations[user_id] >= MAX_VIOLATIONS:
            await message.guild.ban(message.author, reason="Exceeded advertisement violations limit")
            await message.channel.send(f"{message.author.mention} has been banned for exceeding the advertisement violations limit.")
        else:
            await message.channel.send(f"{message.author.mention}, advertising is not allowed in this server. Violation {violations[user_id]}/{MAX_VIOLATIONS}. Please note that when you exceed the maximum violations count, you will be permanently banned from this server.")

        save_violations(VIOLATIONS_FILE, violations)
    else:
        await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    # Assign a role to bots when they join
    if member.bot:
        bot_role = discord.utils.get(member.guild.roles, name="Bots")
        if bot_role is not None:
            await member.add_roles(bot_role)
        else:
            await member.guild.create_role(name="Bots")
            bot_role = discord.utils.get(member.guild.roles, name="Bots")
            await member.add_roles(bot_role)
    else:
        await send_challenge(bot, member)

bot.run(TOKEN)