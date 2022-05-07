import configparser, asyncio, os, sys
import discord
from discord.ext import commands
from config import Config

config = Config()

bot = commands.Bot(command_prefix=config.prefix, case_insensitive=True, description=config.description)

startup_extensions = ["roles", "rng", "owner", "events"]

@bot.command(hide=True)
async def load(ctx, extension_name : str):
    """Load an extension"""
    if ctx.author.id != config.owner:
        return
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send(f"Module { extension_name } loaded.")

@bot.command(hide=True)
async def unload(ctx, extension_name : str):
    """Unload an extension"""
    if ctx.author.id != config.owner:
        return
    bot.unload_extension(extension_name)
    await ctx.send(f"Module { extension_name } unloaded.")

@bot.command(hide=True)
async def reload(ctx, extension_name : str):
    """Reload an extension"""
    if ctx.author.id != config.owner:
        return
    bot.unload_extension(extension_name)
    await asyncio.sleep(1)
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.send(f"```py\n{ type(e).__name__ }: { str(e) }\n```")
    await ctx.send(f"Module { extension_name } reloaded.")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}.", file=sys.stderr)

    bot.run(config.token)