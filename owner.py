import asyncio
import discord
from discord.ext.commands import Cog, command, CheckFailure
from config import Config

config = Config()

# All commands defined here are only for the owner of the bot
class Owner(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Check if the one calling the command is the owner
    async def cog_check(self, ctx):
        if ctx.author.id == config.owner:
            return True

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            print(error)

    async def cog_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Error. No tienes permisos para ejecutar este comando", delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()

    @command(hide=True)
    async def quit(self, ctx):
        """Turns off the bot."""
        await ctx.send("Turning bot off...")
        print("Turning bot off...")
        await asyncio.sleep(5)
        await self.bot.close()
        await self.bot.logout()

    # For testing purposes, prints a message to the console from discord
    @command(hide=True)
    async def console(self, ctx, msg : str):
        """Sends message to the console"""
        print(msg) 
        await ctx.send("Message sent to console", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Owner(bot))