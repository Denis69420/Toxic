import nextcord
from nextcord.ext import commands
from sqlalchemy.orm import sessionmaker
from models import Ticket, engine

Session = sessionmaker(bind=engine)
session = Session()

class TicketSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ticket')
    async def create_ticket(self, ctx, *, reason):
        ticket_channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}')
        ticket = Ticket(channel_id=ticket_channel.id, user_id=ctx.author.id, reason=reason)
        session.add(ticket)
        session.commit()
        await ticket_channel.send(f'Ticket created by {ctx.author.mention} for reason: {reason}')
        await ctx.send(f'Ticket created: {ticket_channel.mention}')

    @commands.command(name='close')
    @commands.has_permissions(manage_channels=True)
    async def close_ticket(self, ctx):
        ticket = session.query(Ticket).filter_by(channel_id=ctx.channel.id).first()
        if ticket:
            session.delete(ticket)
            session.commit()
            await ctx.channel.delete()
        else:
            await ctx.send('This is not a ticket channel.')

def setup(bot):
    bot.add_cog(TicketSystem(bot))
