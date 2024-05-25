from nextcord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send('Hello!')

def setup(bot):
    bot.add_cog(General(bot))
