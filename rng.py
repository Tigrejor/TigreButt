import random
from discord.ext import commands

class RNG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice : str):
        """Tira un dado con formato NdN."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send("El formato debe ser NdN")
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices : str):
        """Elige entre múltiples opciones."""
        await ctx.send(random.choice(choices))

def setup(bot):
    bot.add_cog(RNG(bot))