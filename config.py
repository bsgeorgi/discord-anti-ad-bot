from discord import Intents

# Discord bot token
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Maximum number of violations (advertisement) before bot bans the user
MAX_VIOLATIONS = 3
VIOLATIONS_FILE = 'violations.json'

# Domains that users are allowed to use when posting messages
ALLOWED_DOMAINS = [
    'mydomain.net'
]

# Bot permissions
intents = Intents.default()
intents.guilds = True
intents.messages = True
intents.members = True
intents.message_content = True

# Challenges to send to the user when they first enter the server
challenges = [
    ('Replace the "?" with the correct operator to make the equation true: 4 ? 2 = 2', ['/', 'divide', 'division']),
    ('Replace the "?" with the correct operator to make the equation true: 3 ? 4 = 7', ['+', 'add', 'plus']),
    ('Replace the "?" with the correct operator to make the equation true: 5 ? 3 = 15', ['*', 'multiply', 'times']),
]