import os
import nextcord
from sqlalchemy.orm import sessionmaker
from models import ServerConfig, engine
from tickets.ticket_system import TicketSystem
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True

Session = sessionmaker(bind=engine)
session = Session()

def get_guild_config(guild_id):
    config = session.query(ServerConfig).filter_by(guild_id=str(guild_id)).first()
    if not config:
        config = ServerConfig(guild_id=str(guild_id))
        session.add(config)
        session.commit()
    return config

bot = nextcord.ext.commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    get_guild_config(guild.id)

# Load commands
bot.load_extension('commands.admin')
bot.load_extension('commands.general')

# Load ticket system
bot.add_cog(TicketSystem(bot))

# Load events
import events.member_events
import events.message_events
bot.add_listener(events.member_events.on_member_join)
#bot.add_listener(events.message_events.on_message)

bot.run(os.getenv('DISCORD_TOKEN'))
