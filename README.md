# discord-anti-ad-bot

The Discord Anti-Advertisement Bot is designed to prevent users from posting advertisements on a Discord server. The bot monitors messages and deletes any content that it identifies as advertising. Additionally, the bot sends a challenge to new members to verify that they are not bots.

# Features
1. Detects and deletes advertisement messages.
2. Bans users who exceed the maximum number of advertisement violations.
3. Sends a challenge to new members to verify they are not bots.
4. Automatically assigns a "Bots" role to bots when they join the server.
5. Supports customizable command prefix and challenge questions.

# Bot Permissions
To function correctly, the bot requires the following permissions:

1. Read Messages: To monitor messages in the server.
2. Send Messages: To notify users about their violations and send challenge messages.
3. Manage Messages: To delete advertisement messages.
4. Ban Members: To ban users who exceed the maximum number of violations.
5. Kick Members: To kick users who fail the new member challenge.
6. Manage Roles: To assign roles to bots when they join the server.
