from discord.ext.commands import Command

def setup(bot):
    @bot.command(name='hello')
    async def hello(ctx):
        await ctx.send("Hello!")