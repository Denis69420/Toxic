import nextcord
from nextcord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)  # +1 to delete the purge command message
        await ctx.send(f'Deleted {amount} messages', delete_after=5)

    @commands.command(name='nuke')
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        new_channel = await ctx.channel.clone()
        await ctx.channel.delete()
        await new_channel.send('This channel has been nuked!')

    @commands.command(name='timeout')
    @commands.has_permissions(mute_members=True)
    async def timeout(self, ctx, member: nextcord.Member, minutes: int, *, reason=None):
        await member.edit(mute=True)
        await ctx.send(f'Timed out {member.name} for {minutes} minutes for reason: {reason}')

def setup(bot):
    bot.add_cog(Admin(bot))
