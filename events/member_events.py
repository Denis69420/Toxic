import nextcord

async def on_member_join(member):
    config = get_guild_config(member.guild.id)
    if config.welcome_channel_id:
        welcome_channel = member.guild.get_channel(int(config.welcome_channel_id))
        if welcome_channel:
            welcome_message = config.welcome_message
            if config.verification_enabled:
                welcome_message += ' Please verify yourself.'
            await welcome_channel.send(welcome_message.replace('{member}', member.mention))

async def on_member_leave(member):
    config = get_guild_config(member.guild.id)
    if config.leave_channel_id:
        leave_channel = member.guild.get_channel(int(config.leave_channel_id))
        if leave_channel:
            leave_message = config.leave_message or f'{member.display_name} has left the server.'
            await leave_channel.send(leave_message.replace('{member}', member.mention))