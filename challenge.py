import random
import asyncio
import re
from config import *

# Load our list of advertisement patterns
def load_patterns(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    url_patterns, text_patterns = content.split('\n\n')
    return url_patterns.split('\n'), text_patterns.split('\n')

URL_PATTERNS, TEXT_PATTERNS = load_patterns('patterns.txt')

async def send_challenge(bot, member):
    question, answers = random.choice(challenges)
    channel = await member.create_dm()
    await channel.send(f"Welcome to {member.guild.name}! To verify that you are not a bot, please answer the following question within 30 seconds:\n\n{question}")

    def check(m):
        return m.channel == channel and m.author == member

    # Wait for the user's response and handle the result
    try:
        response = await bot.wait_for('message', check=check, timeout=30)
        if response.content.lower() in [a.lower() for a in answers]:
            await channel.send("Thank you for verifying! You now have access to the server.")
        else:
            await channel.send("Incorrect answer. Please try again by rejoining the server.")
            await member.kick(reason="Failed verification")
    except asyncio.TimeoutError:
        await channel.send("Time's up! Please try again by rejoining the server.")
        await member.kick(reason="Failed verification")

def is_domain_allowed(text):
    for domain in ALLOWED_DOMAINS:
        if re.search(r'\b' + re.escape(domain) + r'\b', text, re.IGNORECASE):
            return True
    return False

# Check for invite links and common advertisement phrases
def is_advertising(text):
    if is_domain_allowed(text):
        return False
    
    for pattern in URL_PATTERNS + TEXT_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False