import discord
import asyncio
from discord.ext.commands import Cog, command, CheckFailure
from discord.utils import get
from config import Config

config = Config()

class Roles(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Check if we are in the right channel
    async def cog_check(self, ctx):
        if ctx.channel.id == config.roles_channel:
            return True

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            print(error)

    # Call the check for the right channel
    async def cog_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Incorrect channel", delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
        else: # If the error is not because of the wrong channel print to console
            print(error)

    @command(hide=True)
    async def role(self, ctx):
        """Shows own roles"""
        roles = ""
        for r in ctx.author.roles:
            print(r)
            print('--')
            roles += str(r) + " "
        await ctx.send("```Your roles are: " + roles + "```")

def setup(bot):
    bot.add_cog(Roles(bot))