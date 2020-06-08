# ____  __.        __________        __
# |    |/ _|        \______   \ _____/  |_
# |      <    ______ |    |  _//  _ \   __\
# |    |  \  /_____/ |    |   (  <_> )  |
# |____|__ \         |______  /\____/|__|
#        \/                \/
# __________           _________             .__
# \______   \___.__.  /   _____/____    ____ |__| ____
# |    |  _<   |  |  \_____  \\__  \  /    \|  |/ ___\
# |    |   \\___  |  /        \/ __ \|   |  \  \  \___
# |______  // ____| /_______  (____  /___|  /__|\___  >
#       \/ \/              \/     \/     \/        \/

import discord
import datetime
from datetime import datetime
from json import load
from discord.ext import commands

client = commands.Bot(command_prefix="k!")

# Load Config #
try:
    with open('config/config.json') as e:
        config = load(e)
        token = config['token']
except Exception as e:
    print(e)
    quit()

# Global Variables #
Sanic = None


@client.event
async def on_ready():
    global Sanic

    print('K-Bot has initialized')
    Sanic = client.get_user(348052878444986370)


# Bot Info #
@client.command()
async def info(ctx):
    global Sanic

    ping = round(client.latency * 1000)

    embed = discord.Embed(
        title='Bot Info',
        colour=discord.Colour.purple()
    )
    embed.add_field(name='`Current Prefix: `', value='k!', inline=False)
    embed.add_field(name='`Bot Owner: `', value=Sanic.mention, inline=False)
    embed.add_field(name='`Ping: `', value=ping, inline=False)

    await ctx.send(embed=embed)


# Command Menu #
@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title=str(ctx.guild.name),
        description='kBot Help Menu!',
        coluor=discord.Colour.green()
    )

    embed.add_field(
        name='kBot Commands',
        value="`k!uptime` `k!rules` `k!av` `k!suggest` `k!info`",
        inline=False
    )

    embed.add_field(
        name='kBot Customization',
        value="`k!setstatus` `k!setactivity`",
        inline=False
    )

    embed.add_field(
        name='Administrator Page',
        value="`k!announce` `k!clear` `k!lock` `k!unlock` `k!setgame` `k!poll`",
        inline=False
    )

    await ctx.send(embed=embed)


# Avatar Finder #
@client.command()
async def av(ctx, arg):
    try:
        message = ctx.message
        for x in message.mentions:
            await ctx.send(x.avatar_url)
            await ctx.send(f'Avatar of {x.mention}')
    except Exception as e:
        print(e)


# Rules #
@client.command()
async def rules(ctx):
    rules = discord.File('graphics/Rules.png')

    await ctx.author.send(file=rules)
    await ctx.author.send(
        """[1] → You must comply with the Discord TOS and Guidelines.

[2] → Do not spam in the main chat or any other chat, otherwise you'll get banned permanently.

[3] → Mic Spamming/Channel surfing in Voice Channels is not permitted.

[4] → Do not advertise in our server, do not put any discord servers in main chat, DM'S or any channel, to promote it.

[5] → Keep conversations in English only.

[6] → Begging for a roles or permissions is against the rules, you'll either have to be active, and earn it.

[7] → Threatening someone here, will result in a direct ban.

[8] → Any inappropriate profile, or inappropriate nicknames will get banned, you'll get a mention before you get banned to change it.
⠀
[9] → You can mention staff only if they are needed for anything, please do not mention them for no reason.
⠀
[10] → Post images in the appropriate channel, and use the available channels for what they were created for.

[11] → No nsfw in main chat, or any channels, just keep it in the nsfw section down below, and please keep main chat sfw/friendly/clean.

[12] → Do not execute bot commands in any other text channels than the designated channels provided. Also ensuring you do not command spam.

[13] → Don't argue with staff, decisions are made final, so please respect the staff team, such as the owner/co, admins, mods and the helpers.

[14]→ Automating the bots in this discord is allowed, so have fun <3"""
    )


@client.command()
async def suggest(ctx, *, suggestion=None):
    suggchan = client.get_channel(716727371188666482)

    embed = discord.Embed(
        title='Suggestion!',
        description=suggestion,
        colour=discord.Colour.blue()
    )

    embed.set_footer(
        text=f'submitted by {ctx.author.name} at {datetime.now()}',
        icon_url=ctx.author.avatar_url
    )

    reactions = await suggchan.send(embed=embed)
    await reactions.add_reaction('👍')
    await reactions.add_reaction('👎')

try:
    client.run(token)
except Exception as e:
    print(e)
