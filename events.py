from discord.ext import commands
from discord.utils import get
from config import Config

config = Config()

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == config.server: # Currently checking for specific server, have to change it so it checks into a database to define different roles for different servers
            role = get(member.guild.roles, name="Wolves") # Role hardcoded since first version of the bot, have to add some kind of database for different servers and roles
            await member.add_roles(role)
        print('New member')
        print('------')
        print('')

    # Best way to check bot went alive
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')
        print('')

def setup(bot):
    bot.add_cog(Events(bot))
