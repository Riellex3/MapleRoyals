# bot.py
import os
import random
import pathlib
import time
import datetime
import asyncio
from itertools import cycle
import json
import csv

import math
from datetime import date
import discord
from discord import channel
from discord.ext import commands, tasks
from dotenv import load_dotenv
from PIL import Image, ImageSequence, ImageDraw, ImageFont
from io import BytesIO

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# Enables intents for bot to detect members list
# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents=intents)

#initialize bot
bot = commands.Bot(command_prefix='~', case_insensitive=True)
print('Running...')

dir_path = os.path.dirname(os.path.realpath(__file__))

# alleventtimes= ['00:00','01:00','03:00','04:00','05:00','07:00','08:00','09:00','11:00','12:00','13:00','15:00','16:00','17:00','19:00','20:00','21:00','23:00']
voteremindertimes=['12:00','23:00']
# testeventreminder=['08:37']

bosstimerList=[[-1 for j in range(20)] for i in range(42)]
bossList = [['mano',3],['stumpy',3],['deo',3],['king_clang',3],['seruf',3],['faust',3],['giant_centipede',3],['timer',3],['mushmom',3],['dyle',3],['zombie_mushmom',3],['zeno',3],['nine-tailed_fox',3],['tae_roon',3],['king_sage_cat',3],['jrbalrog',3],['eliza',3],['snack_bar',3],['chimera',3],['blue_mushmom',23],['snowman',3],['headless_horseman',6],['manon',3],['griffey',3],['pianus_left',24],['pianus_right',16],['bigfoot',12],['black_crow',23],['leviathan',2],['kacchuu_musha',11],['dodo',3],['anego',5],['lilynouch',3],['lyka',3],['bftp1',12],['bftp2',12],['bftp3',12],['bftp4',12],['bftp5',12],['bffp',12],['bfed',12],['bfer',12]]



#################################################################################### Discord Features
# Author
@bot.command(name='author', help='About the author')
async def author(ctx):
    await ctx.send('Author: Rielle (Riellex3)')
    await ctx.send('Thank you for using my bot! Please feel free to reach out to me if you have any questions/suggestions for improvement!')
    await ctx.send(file=discord.File(dir_path+'/rie.png'))

@tasks.loop(seconds = 60)
async def minutetimer():
    serverTime=time.gmtime()
    print(f'The current time is: {time.strftime("%H:%M:%S", serverTime)}')

@bot.event
async def on_ready():
    minutetimer.start()
    print(f'Establishing connection in {len(bot.guilds)} guilds...')
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name='MapleRoyals'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(ctx)
        await ctx.send('Invalid arguments. Please type \"~help [command]\" for more information.')
    elif isinstance(error, commands.CommandNotFound):
        print(ctx)
        await ctx.send('Invalid command uwu. Please type \"~help\" for a list of available commands.')
    else:
        print(ctx)
        await ctx.send('Oops. Something went wrong.', delete_after=5)
        raise error

# Return avatar of the user
@bot.command(name = 'avatar', help = 'Return avatar of the user')
async def feed(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    asset = user.avatar_url_as(format='png', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)
    pfp.save('profile.png')
    await ctx.send(file = discord.File("profile.png"))

# Boba
@bot.command(name = 'boba', help = 'Give the user boba')
async def boba(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    boba = Image.open(dir_path + '/boba.gif')

    asset = user.avatar_url_as(format='png', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)

    frames = []
    for frame in ImageSequence.Iterator(boba):
        frame = frame.copy()
        frame=frame.convert('RGBA')
        pfp.paste(frame, (40,80), frame)
        pfp.save('profile.png')
        frames.append(pfp)
        pfp = Image.open(data)
        pfp.thumbnail((128,128), Image.ANTIALIAS)
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
    await ctx.send(file = discord.File("profile.gif"))

# Noodle
@bot.command(name = 'noodle', help = 'Give the user noodles')
async def noodle(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    noodle = Image.open(dir_path + '/noodle.gif')

    asset = user.avatar_url_as(format='png', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)

    frames = []
    for frame in ImageSequence.Iterator(noodle):
        frame = frame.copy()
        frame=frame.convert('RGBA')
        pfp.paste(frame, (30,82), frame)
        pfp.save('profile.png')
        frames.append(pfp)
        pfp = Image.open(data)
        pfp.thumbnail((128,128), Image.ANTIALIAS)
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)
    await ctx.send(file = discord.File("profile.gif"))

@bot.command(name = 'slap', help = 'Slap!')
async def slap(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    
    slap = Image.open('slap.gif')
    

    asset = user.avatar_url_as(format = 'jpg', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)
    pfp = pfp.convert('RGBA')


    frames = [f.copy() for f in ImageSequence.Iterator(slap)]
    for i, frame in enumerate(frames):
        frame = frame.convert("RGBA")
        if i < 21:
            frame.paste(pfp, (310, 95))
        elif i < 27:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))
        elif i < 30:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (290, 40))
        elif i < 31:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))
        elif i < 33:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))    
        elif i < 35:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (350, 60))   
        else:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (350, 65))
        
        frames[i] = frame
    
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=40, loop=0)
    await ctx.send(file = discord.File('profile.gif'))

# Display Area Boss Timers
@bot.command(name='bosstimer', help = 'Displays Area Boss Timers')
async def bosstimer(ctx):
    embed1 = discord.Embed(color = discord.Colour.blue())
    embed1.description = 'Here are the timers for area bosses\n\n**Mano:** 3 Hours\n**Stumpy:** 3 Hours\n**Deo:** 3 Hours\n**King Clang:** 3 Hours\n**Seruf:** 3 Hours\n**Faust:** 3 Hours\n**Giant Centipede:** 3 Hours\n**Timer:** 3 Hours\n**Mushmom:** 3 Hours\n**Dyle:** 3 Hours\n**Zombie Mushmom:** 3 Hours\n**Zeno:** 3 Hours\n**Nine-Tailed Fox:** 3 Hours\n**Tae Roon:** 3 Hours\n**King Sage Cat:** 3 Hours\n**Jr. Balrog:** 3 Hours\n**Eliza:** 3 Hours\n\nPage 1 of 2'

    embed2 = discord.Embed(color = discord.Colour.blue())
    embed2.description = 'Here are the timers for area bosses\n\n**Snack Bar:** 3 Hours\n**Chimera:** 3 Hours\n**Blue Mushmom:** 23 Hours\n**Snowman:** 3 Hours\n**Headless Horseman:** 6 Hours\n**Manon:** 3 Hours\n**Griffey:** 3 Hours\n**Pianus(Left):** 24 Hours\n**Pianus(Right):** 16 Hours\n**Bigfoot:** 12 Hours\n**Black Crow:** 23 Hours\n**Leviathan:** 2 Hours\n**Kacchuu Musha:** 11 Hours\n**Dodo:** 3 Hours\n**Anego:** 5 Hours\n**Lilynouch:** 3 Hours\n**Lyka:** 3 Hours\n\nPage 2 of 2'
    message = await ctx.send(embed = embed1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')


    def check(reaction, user):
        return user == ctx.author

    reaction = None

    while True:
        if str(reaction) == '◀':
            await message.edit(embed = embed1)
        elif str(reaction) == '▶':
            await message.edit(embed = embed2)
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions() 

@bot.command(name = 'cs', help = 'Simulates a chaos scroll')
async def cs(ctx, *argv: int):
    P5 = 0.99
    P4 = 1.98
    P3 = 10.21
    P2 = 15.87
    P1 = 19.31
    P0 = 18.38
    P_1 = 13.70
    P_2 = 8.00
    P_3 = 3.65
    P_4 = 2.97
    P_5 = 4.94

    R5 = P5
    R4 = R5 + P4
    R3 = R4 + P3
    R2 = R3 + P2
    R1 = R2 + P1
    R0 = R1 + P0
    R_1 = R0 + P_1
    R_2 = R_1 + P_2
    R_3 = R_2 + P_3
    R_4 = R_3 + P_4
    R_5 = R_4 + P_5
    stats = ''
    cses = ''
    
    if not argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = str(cs)
    
    for arg in argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = cses + str(cs) + ' '
        if arg == 0:
            result = arg
            stats = stats + str(result) + '\n'
            continue
        result = arg+cs
        if result < 0:
            result = 0
        stats = stats + str(result) + '\n'
    
    pf = round(random.random(),2)
    if pf > 0.6:
        await ctx.send(file = discord.File('scrollfailed.gif'))
        return
    await ctx.send(file = discord.File('scrollpassed.gif'))
    await asyncio.sleep(2)
    if argv:
        await ctx.send(f'Your cs boosted your stats by {cses}\nYour new stats are\n{stats}')
    else:
        await ctx.send(f'Your cs boosted your stats by {cses}')

@bot.command(name = 'csp', help = 'Simulates a successful chaos scroll')
async def csp(ctx, *argv: int):
    P5 = 0.99
    P4 = 1.98
    P3 = 10.21
    P2 = 15.87
    P1 = 19.31
    P0 = 18.38
    P_1 = 13.70
    P_2 = 8.00
    P_3 = 3.65
    P_4 = 2.97
    P_5 = 4.94

    R5 = P5
    R4 = R5 + P4
    R3 = R4 + P3
    R2 = R3 + P2
    R1 = R2 + P1
    R0 = R1 + P0
    R_1 = R0 + P_1
    R_2 = R_1 + P_2
    R_3 = R_2 + P_3
    R_4 = R_3 + P_4
    R_5 = R_4 + P_5
    stats = ''
    cses = ''
    
    if not argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = str(cs)
    
    for arg in argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = cses + str(cs) + ' '
        result = arg+cs
        if arg == 0:
            result = arg
            stats = stats + str(result) + '\n'
            continue
        if result < 0:
            result = 0
        stats = stats + str(result) + '\n'
    
    await ctx.send(file = discord.File('scrollpassed.gif'))
    await asyncio.sleep(2)
    if argv:
        await ctx.send(f'Your cs boosted your stats by {cses}\nYour new stats are\n{stats}')
    else:
        await ctx.send(f'Your cs boosted your stats by {cses}')

# Get servertime
@bot.command(name = 'servertime', help = 'States the current servertime')
async def servertime(ctx):
    serverTime=time.gmtime()
    await ctx.send(f'The current time is: {time.strftime("%H:%M:%S", serverTime)}')
    

####################################################################################

# Orbis etc. GUIDE
@bot.command(name='orbisetc',help='Displays Orbis Etc. Guide')
async def orbisetc(ctx):
    await ctx.send(file=discord.File(dir_path+'/orbisetc.png'))

# Leech GUIDE
@bot.command(name='leech',help='Displays Leech Guide')
async def leech(ctx):
    await ctx.send(file=discord.File(dir_path+'/leech.png'))

# Mage 1hit GUIDE
@bot.command(name='mage1hit',help='Displays Mage Magic 1-hit Breakpoints')
async def mage1hit(ctx):
    await ctx.send(file=discord.File(dir_path+'/mage1hit.jpg'))


# BF GUIDE
@bot.command(name='bigfoot',help='Displays Bigfoot Guide by Sparky95')
async def bigfoot(ctx):
    await ctx.send(file=discord.File(dir_path+'/bigfoot.png'))

#################################################################################### PALA
# Pala GUIDE
@bot.command(name='pala',help='Displays Paladin Guide')
async def pala(ctx):
    await ctx.send(file=discord.File(dir_path+'/pala.png'))

# Pala CWK GUIDE
@bot.command(name='palaCWK',help='Displays Paladin CWK Guide')
async def palacwk(ctx):
    await ctx.send(file=discord.File(dir_path+'/palacwk.png'))

# Pala ZAK GUIDE
@bot.command(name='palaZAK',help='Displays Paladin ZAK Guide')
async def palazak(ctx):
    await ctx.send(file=discord.File(dir_path+'/palazak.png'))

# Pala HT GUIDE
@bot.command(name='palaHT',help='Displays Paladin HT Guide')
async def palaht(ctx):
    await ctx.send(file=discord.File(dir_path+'/palaht.png'))

# Pala NT GUIDE 1
@bot.command(name='palant',help='Displays Paladin NT Guide')
async def palant(ctx):
    await ctx.send(file=discord.File(dir_path+'/palant.png'))


####################################################################################

# Boss Weaknesses
@bot.command(name='bossinfo',help='Displays Various Boss Weaknesses')
async def bossinfo(ctx):
    await ctx.send(file=discord.File(dir_path+'/bossinfo.png'))

# Toad
@bot.command(name='palatoad',help='Displays Toad Elemental Weaknesses')
async def toad(ctx):
    await ctx.send(file=discord.File(dir_path+'/toad.png'))

# Boss HP/EXP Info
@bot.command(name='bossexp',help='Displays Boss HP/EXP Info')
async def bossexp(ctx):
    await ctx.send('(taken from hiddenstreet) \nPapulatus: [8.03:1] 23,000,000 HP : 2,860,800 EXP \nZakum: [9.54:1] 482,100,000 HP : 50,498,560 EXP (may not be right exp/ratio) \nKrex: [8.68:1] 500,000,000 HP : 57,600,000 EXP (taken from Joong) \nScarlion/Targa: [15.5:1] 300,000,000 HP : 19,353,600 EXP \nScarlion+Targa (both in corner): [~7.75-11.62:1] ~300,000,000-450,000,000 HP : 37,707,200 EXP \nHorntail: [7.93:1] 2,730,000,000 HP : 344,146,432 EXP (from ilyssia''s chart) \nToad: [6.98:1] 1,070,000,000 HP : 153,120,000 EXP \nThe Boss (total): [7.84:1] 1,050,000,000 HP : 133,760,000 EXP (may not be right exp/ratio) \nShao: [1.95:1] 100,000,000 HP : 51,200,000 EXP')

# HP Quest
@bot.command(name='hpquest',help='Displays HP Quest Info')
async def hpquest(ctx):
    await ctx.send(file=discord.File(dir_path+'/hpquest.png'))


# CWK GUIDE
@bot.command(name='cwkguide', help='Displays CWK Guide')
async def cwkguide(ctx):
    embed = discord.Embed(color = discord.Colour.blue())
    embed.description = 'https://mapleroyals.com/forum/threads/crimsonwood-party-quest-prequisite-guide-2020-cwpq.153541/'

    await ctx.send(embed=embed, file=discord.File(dir_path+'/cwk.png'))

# GPQ GUIDE
@bot.command(name='gpqguide', help='Displays GPQ Guide')
async def gpqguide(ctx):
    embed = discord.Embed(color = discord.Colour.blue())
    embed.description = 'https://mapleroyals.com/forum/threads/gpq-guide-2021-revamped.199116/'

    await ctx.send(embed=embed, file=discord.File(dir_path+'/gpqguide.png'))

# APQ GUIDE
@bot.command(name = 'apqguide',help='Displays APQ Guide')
async def apqguide(ctx):
    embed = discord.Embed(color = discord.Colour.blue())
    embed.description = 'https://mapleroyals.com/forum/threads/comprehensive-apq-guide-updated-feb-2021.172942/'
    await ctx.send(embed=embed, file=discord.File(dir_path+'/apq.png'))

# OPQ GUIDE
@bot.command(name = 'opqguide',help='Displays OPQ Guide')
async def apqguide(ctx):
    embed = discord.Embed(color = discord.Colour.blue())
    embed.description = 'https://mapleroyals.com/forum/threads/orbis-pq-guide.174277/'
    await ctx.send(embed=embed, file=discord.File(dir_path+'/apq.png'))
    

# HP Washing Info
@bot.command(name='HPwashInfo', help = 'Displays info for HP Washing')
async def hpwashinfo(ctx):
    #info = ('Here''s some data for HP washing by adding the point to HP using an AP reset, and then removing it using another reset\nJob, HP gained, MP lost, Min MP, Min HP\nBeginner, +8~12HP, -8MP, (10 x level) +2\nSpearman/Paladin, +50~55HP, -4MP, (4 x level) +156\nHero, +50-55HP, -4MP, (4 x level) +56\nThief, +16~20HP (20-24HP Fresh AP), -12MP, (14 x level) +156\nBowman, +16~20HP, -12MP, (14 x level) +148\nMagician, +10~20HP, -90MP, (14 x level) +148\nPirate, +20HP (+40HP for Brawlers), -16MP, (18 x level) +111')
    await ctx.send(file=discord.File(dir_path+'/hpwash.png'))

# HP Washing Calculator
@bot.command(aliases=['wash','washes','hpwash'], help = 'Calculates how many times the character can wash based on their current level and extra MP\n ~hpwash <job> <level> <Total MP without Equips>\nAcceptable jobs are: \nwarrior, swordman, fighter, crusader, hero, page, whiteknight, paladin, pala, pally, spearman, dragonknight, darkknight, dk\n\narcher, bowman, hunter, ranger, bowmaster, bm, crossbowman, crossbowwoman, sniper, marksman, mm\n\nthief, rogue, assassin, sin, hermit, nightlord, nl, bandit, dit, chiefbandit, cb, shadower, shad\n\nbrawler, marauder, buccaneer, bucc\n\ngunslinger, slinger, outlaw, corsair, sair\n\nmagician, cleric, priest, bishop, bish, bs, wizard, mage, archmage, am')
async def hpwashing(ctx, job, level, mp, *argv):
    #ctx.send('HP Washing Feature is currently under maintenance...')
    #return
    
    minMP = 0
    aprHP = 0
    minusAprMP = 0
    washedHP = 0
    freshHP = 0
    aprHPmin = 0
    aprHPmax = 0
    freshAP = 0

    try:
        int(level)
    except ValueError:
        await ctx.send('Please enter a valid level\n``~hpwash <job> <level> <MP without Equips>``')
        return
    try:
        int(mp)
    except ValueError:
        await ctx.send('Please enter a valid mp\n``~hpwash <job> <level> <MP without Equips>``')
        return

    try:
        int(argv[0])
    except ValueError:
        await ctx.send('Please enter a valid amount of fresh AP\n``~hpwash <job> <level> <MP without Equips>``')
        return
    except IndexError:
        pass
    else:
        freshAP = int(argv[0])
        pass
    

    level = int(level)
    mp = int(mp)

    if level < 1 or level > 200:
        await ctx.send(f'Your level must be 1-200')
        await ctx.send('``~hpwash <job> <level> <MP without Equips>``')        
        return
    # Here's some data for those who already know about HP Washing:
    # Job, HP gained, MP lost, Min MP, Min HP
    # Beginner, +8~12HP, -8MP, (10 x level) +2, (12 x level) +50
    # Warrior, +50~54HP, -4MP, (4 x level) +156, (24 x level) +172
    # Thief, +20~24HP, -12MP, (14 x level) +156, (24 x level) +472
    # Bowman, +16~20HP, -12MP, (14 x level) +148, (20 x level) +378
    # Magician, +6~10HP, -90MP, (14 x level) +148, (20 x level) +378
    # Pirate, +16~20HP (+36~40HP for Brawlers), -16MP, (18 x level) +111, (22 x level) +380

    # Here's some data for HP washing by adding the point to HP using an AP reset, and then removing it using another reset:
    # Job, HP gained, MP lost, Min MP, Min HP
    # Beginner, +8~12HP, -8MP, (10 x level) +2
    # Spearman/Paladin, +50~55HP, -4MP, (4 x level) +156
    # Hero, +50-55HP, -4MP, (4 x level) +56
    # Thief, +16~20HP (20-24HP Fresh AP), -12MP, (14 x level) +156
    # Bowman, +16~20HP, -12MP, (14 x level) +148
    # Magician, +10~20HP, -90MP, (14 x level) +148
    # Pirate, +20HP (+40HP for Brawlers), -16MP, (18 x level) +111
    accepted_strings_Warrior = ['warrior','swordman','fighter','crusader','hero','page','whiteknight','paladin','pala','pally','spearman','dragonknight','darkknight','dk']
    accepted_strings_Warrior2 =['fighter','crusader','hero']
    accepted_strings_Archer = ['archer','bowman','hunter','ranger','bowmaster','bm','crossbowman','crossbowwoman','sniper','marksman','mm']
    accepted_strings_Thief = ['thief','rogue','assassin','sin','hermit','nightlord','nl','bandit','dit','chiefbandit','cb','shadower','shad']
    accepted_strings_Brawler = ['brawler','marauder','buccaneer','bucc']
    accepted_strings_Sair = ['gunslinger','slinger','outlaw','corsair','sair']
    accepted_strings_Mage = ['magician','cleric','priest','bishop','bish','bs','wizard','mage','archmage','am']

    if job in accepted_strings_Warrior:
        minMP = level*4+156
        if job in accepted_strings_Warrior2:
            minMP = level*4+56
        aprHPmin = 50
        aprHPmax = 55
        aprHP = 53
        minusAprMP = 4
    elif job in accepted_strings_Archer:
        minMP = level*14+148
        aprHPmin = 16
        aprHPmax = 20
        aprHP = 18
        minusAprMP = 12
    elif job in accepted_strings_Thief:
        minMP = level*14+156
        aprHPmin = 16
        aprHPmax = 20
        aprHP = 18
        freshHPmin = 20
        freshHPmax = 24
        freshHP = 22
        minusAprMP = 12
    elif job in accepted_strings_Brawler:
        minMP = level*18+111
        aprHPmin = 40
        aprHPmax = 40
        aprHP = 40
        minusAprMP = 16
    elif job in accepted_strings_Sair:
        minMP = level*18+111
        aprHPmin = 40
        aprHPmax = 40
        aprHP = 20
        minusAprMP = 16
    elif job in accepted_strings_Mage:
        minMP = level*22+488
        aprHPmin = 10
        aprHPmax = 20
        aprHP = 15
        minusAprMP = 30
    else:
        sep = ""
        await ctx.send(f'Please state the job correctly\nAcceptable jobs are: \nwarrior, swordman, fighter, crusader, hero, page, whiteknight, paladin, pala, pally, spearman, dragonknight, darkknight, dk\n\narcher, bowman, hunter, ranger, bowmaster, bm, crossbowman, crossbowwoman, sniper, marksman, mm\n\nthief, rogue, assassin, sin, hermit, nightlord, nl, bandit, dit, chiefbandit, cb, shadower, shad\n\nbrawler, marauder, buccaneer, bucc\n\ngunslinger, slinger, outlaw, corsair, sair\n\nmagician, cleric, priest, bishop, bish, bs, wizard, mage, archmage, am')
        await ctx.send('``~hpwash <job> <level> <MP without Equips>``')
        return
        #{*accepted_strings_Archer, sep = ", "}\n{*accepted_strings_Thief, sep = ", "}\n{*accepted_strings_Brawler, sep = ", "}\n{*accepted_strings_Sair, sep = ", "}\n{*accepted_strings_Mage, sep = ", "}

    numAPRs = int(round((mp-minMP)/minusAprMP))
    if numAPRs <= 0:
        numAPRs = 0
        washedHP = 0
        await ctx.send(f'You cannot wash based on these credentials')
        return

    washedHPmin = aprHPmin*numAPRs
    washedHPmax = aprHPmax*numAPRs        
    washedHP = aprHP*numAPRs

    # Pirates get a static 40 HP from aprs
    if job in accepted_strings_Brawler or job in accepted_strings_Sair:
        await ctx.send(f'Your minimum MP is {"{:,}".format(minMP)}\nYour extra mp is {"{:,}".format(mp-minMP)}\nYou can wash with APR {"{:,}".format(numAPRs)} times and gain an approximate of **{"{:,}".format(washedHP)}** HP')
        return
    
    # Return statement for non-pirates
    await ctx.send(f'Your minimum MP is {"{:,}".format(minMP)}\nYour extra mp is {"{:,}".format(mp-minMP)}\nYou can wash with APR {"{:,}".format(numAPRs)} times and gain {"{:,}".format(washedHPmin)} - {"{:,}".format(washedHPmax)} **({"{:,}".format(washedHP)} average)** HP')
    
    # If user wants to wash thief with fresh AP first before APR    
    if job in accepted_strings_Thief and freshAP > 0:
        washedfreshHPmin = freshAP * freshHPmin
        washedfreshHPmax = freshAP * freshHPmax
        washedfreshHP = freshAP * freshHP
        mp = mp-freshAP*minusAprMP
        numAPRs = int(round((mp-minMP)/minusAprMP))
        washedHPmin = aprHPmin*numAPRs
        washedHPmax = aprHPmax*numAPRs        
        washedHP = aprHP*numAPRs

    # Extra return for thieves
    if job in accepted_strings_Thief and freshAP > 0:
        await ctx.send(f'||As a thief, you can wash with fresh AP up to {"{:,}".format(freshAP)} times and gain {"{:,}".format(washedfreshHPmin)} - {"{:,}".format(washedfreshHPmax)} **({"{:,}".format(washedfreshHP)} average)**\nYou can then wash with APRs up to {"{:,}".format(numAPRs)} times and gain {"{:,}".format(washedHPmin)} - {"{:,}".format(washedHPmax)} **({"{:,}".format(washedHP)} average)** HP\nTotal HP gained from this method: {"{:,}".format(washedfreshHPmin + washedHPmin)} - {"{:,}".format(washedfreshHPmax + washedHPmax)} **({"{:,}".format(washedfreshHP+washedHP)} average)** HP||')
        return
    if job in accepted_strings_Thief:
        await ctx.send(f'If you plan to wash with Fresh AP as well, you may use the command below\n~hpwash thief <level> <MP without equips> <# of fresh AP>')

#Physical Damage Range Calculator
@bot.command(name = 'attrange', help = 'Calculates the attack range given the weapon, str, dex, int, luk, and weapon attack\nAvailable weapons are: 1hsword, 2hsword, 1haxe, 2haxe, 1hbw, 2hbw, spear, polearm, dagger, claw, bow, xbow, knuckle, gun')
async def attrange(ctx, wep: str, strx: float, dexx: float, intx: float, lukx: float, wattx: float):
    if wep == '1hsword':
        maxprimary = strx * 4.0
        minprimary = maxprimary
        secondary = dexx
        mastery = 0.6
    elif wep == '1haxe' or wep == '1hbw':
        maxprimary = strx * 4.4
        minprimary = strx * 3.2
        secondary = dexx
        mastery = 0.6
    elif wep == '2hsword':
        maxprimary = strx * 4.6
        minprimary = strx * 4.6
        secondary = dexx
        mastery = 0.6
    elif wep == '2haxe' or wep == '2hbw':
        maxprimary = strx * 4.8
        minprimary = strx * 3.4
        secondary = dexx
        mastery = 0.6
    elif wep == 'spear' or wep == 'polearm':
        maxprimary = strx * 5.0
        minprimary = strx * 3.0
        secondary = dexx
        mastery = 0.8
    elif wep == 'dagger' or wep == 'claw':
        maxprimary = lukx * 3.6
        minprimary = maxprimary
        secondary = strx + dexx
        mastery = 0.6
    elif wep == 'bow':
        maxprimary = dexx * 3.4
        minprimary = maxprimary
        secondary = strx
        mastery = 0.9
    elif wep == 'xbow':
        maxprimary = dexx * 3.6
        minprimary = maxprimary
        secondary = strx
        mastery = 0.9
    elif wep == 'knuckle':
        maxprimary = strx * 4.8
        minprimary = maxprimary
        secondary = dexx
        mastery = 0.6
    elif wep == 'gun':
        maxprimary = dexx * 3.6
        minprimary = maxprimary
        secondary = strx
        mastery = 0.6
    else:
        await ctx.send('Invalid weapon. Available weapons are: 1hsword, 2hsword, 1haxe, 2haxe, 1hbw, 2hbw, spear, polearm, dagger, claw, bow, xbow, knuckle, gun')
        return
    min = math.floor((minprimary * 0.9 * mastery + secondary) * wattx/100)
    max = math.floor((maxprimary + secondary) * wattx/100)
    await ctx.send(f'{min} ~ {max}')

@bot.command(name = 'whatdrops', help = 'Displays what monster drops a certain item')
async def whatdrops(ctx, *args):
    f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
    msg = ""
    item = ""
    for arg in args:
        item = item + arg + ' '
    item = item.strip().lower()

    for detail in data:
        drops = detail["drops"]
        for drop in drops:
            if item == drop['name'].lower():
                msg = msg + detail["name"] + ", "
    if msg == '':
        await ctx.send(f'Nothing drops {item}')
    else:
        msg = msg[:-2]
        await ctx.send(msg)

@bot.command(name = 'whatis', help = 'Displays mob information')
async def whatis(ctx, *args):
    mob = ""
    for arg in args:
        mob = mob+arg + ' '
    mob = mob.strip()
    mobName = mob.replace(" ","").lower()

    mobList = []
    if mobName == 'list':
        f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
        data = json.load(f)
        f.close()
        for detail in data:
            mobList.append(str(detail["name"]))

        pages = []
        mobCount = 0
        pageLimit = 10
        pageCount = 1
        while True:
            while mobCount < pageLimit:
                desc = '\n'.join(mobList[mobCount:pageLimit])
                page = discord.Embed(title = f'Page {pageCount}', color = discord.Colour.blue())
                page.add_field(name = '** **', value = desc, inline = True)
                mobCount = pageLimit
                pageLimit = pageLimit + 10
                if mobCount >= len(mobList):
                    pages.append(page)
                    break
                desc = '\n'.join(mobList[mobCount:pageLimit])
                page.add_field(name = '** **', value = desc)
                pages.append(page)
                mobCount = pageLimit
                pageLimit = pageLimit + 10
                pageCount = pageCount + 1
                if mobCount >= len(mobList):
                    pageCount = pageCount - 1
                    break
            break
        pageCount = pageCount - 1
        
        message = await ctx.send(embed = pages[0])
        await message.add_reaction('⏮')
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('⏭')

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == '⏮':
                i = 0
                await message.edit(embed = pages[i])
            elif str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '▶':
                if i < pageCount:
                    i += 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '⏭':
                i = pageCount
                await message.edit(embed = pages[i])
            
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break

        await message.clear_reactions() 

        return

    try:
        File=discord.File(dir_path+'/mobs/'+mobName+'.gif')
    except FileNotFoundError:
        await ctx.send(f"{mob} is not in the database.")
        return
    f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
    drops = ""
    dropList = []
    dropList2 = []
    for detail in data:
        if mobName == str(detail["name"]).replace(" ","").lower():
            moob = str(detail["name"])
            dropTab = detail["drops"]
            for drop in dropTab:
                drops = drops + drop["name"] + ", "
                dropList.append(drop["name"] + '\n')
                dropList2.append(drop["name"])
            drops = drops[:-2]
            break
    desc = "N/A"
    if mobName == "splats":
        desc = "Problem child"
    if mobName == "xves":
        desc = "Finisher of goals. Responds to \"God\" or \"Mine Idol\""
    if mobName == "blacephalon":
        desc = "Keep eat"
    if mobName == "uouoy":
        desc = "87"
    if mobName == "soladuck":
        desc = "Naughty"
    if mobName == "loaft":
        desc = "Evolved Monkey"
    if mobName == "gewn":
        desc = "Cat Lover"
    if mobName == "riellex3":
        desc = "Queen"    

    file = discord.File(dir_path+'/mobs/'+mobName+'.gif', filename = 'image.gif')
    embed = discord.Embed(color = discord.Colour.blue())
    embed.add_field(name = "Name", value = moob, inline = False)
    embed.add_field(name = "Description", value = desc, inline = False)
    # embed.add_field(name = "Drops", value = drops[0:int(len(dropList)/2)])
    dropList.sort()

    # Sort into Equips, Use, Setup, Etc.
    f = open(dir_path+"/itemArray.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
 
    #Fetch Level, HP, Resistances, Vulnerabilities, Immunities from mobs.csv
    mobcsvFile = open(dir_path+'/mobs.csv')
    csvreader = csv.reader(mobcsvFile)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    for row in rows:
        if mobName == str(row[0]).replace(" ","").lower():
            mobLevel = row[1]
            mobHP = row[2]
            mobResistances = row[3]
            mobWeaknesses = row[4]
            mobImmunities = row[5]
            mobLocation = row[6]
    mobcsvFile.close()
    embed.add_field(name = "Level", value = mobLevel, inline = True)
    embed.add_field(name = "HP", value = mobHP, inline = True)
    embed.add_field(name = "Resistances", value = mobResistances, inline = True)
    embed.add_field(name = "Weaknesses", value = mobWeaknesses, inline = True)
    embed.add_field(name = "Immunities", value = mobImmunities, inline = True)
    embed.add_field(name = "Notable Location(s)", value = mobLocation, inline = True)

    equips = []
    uses = []
    setup = []
    etc = []
    nx = []
    unknowns = []
    for drop in dropList2:
        for item in data:
            if drop == str(item["name"]):
                if str(item["itemType"]) == 'equip':
                    equips.append(drop + '\n')
                elif str(item["itemType"]) == 'use':
                    uses.append(drop + '\n')
                elif str(item["itemType"]) == 'setup':
                    setup.append(drop + '\n')
                elif str(item["itemType"]) == 'etc':
                    etc.append(drop + '\n')
                elif str(item["itemType"]) == 'nx':
                    nx.append(drop + '\n')
                else:
                    unknowns.append(drop + '\n')
                break
    equips.sort()
    uses.sort()
    setup.sort()
    etc.sort()
    nx.sort()

    embed.add_field(name = 'Drops', value = '** **', inline = False)
    if len(''.join(equips)) > 1000 and equips:
        embed.add_field(name = "Equip", value = ''.join(equips[0:int(len(equips))]))
        embed.add_field(name = '** **', value = ''.join(equips[int(len(equips))::]))
    elif equips:
        embed.add_field(name = 'Equip', value = ''.join(equips), inline = True)
    
    if len(''.join(uses)) > 1000 and uses:
        embed.add_field(name = "Use", value = ''.join(uses[0:int(len(uses)/2)]))
        embed.add_field(name = '** **', value = ''.join(uses[int(len(uses)/2)::]))
    elif uses:
        embed.add_field(name = 'Use', value = ''.join(uses), inline = True)
    
    if len(''.join(setup)) > 1000 and setup:
        embed.add_field(name = "Setup", value = ''.join(setup[0:int(len(setup))]))
        embed.add_field(name = '** **', value = ''.join(setup[int(len(setup))::]))
    elif setup:
        embed.add_field(name = 'Setup', value = ''.join(setup), inline = True)

    if len(''.join(etc)) > 1000 and etc:
        embed.add_field(name = "Etc", value = ''.join(etc[0:int(len(etc))]))
        embed.add_field(name = '** **', value = ''.join(etc[int(len(etc))::]))
    elif etc:
        embed.add_field(name = 'Etc', value = ''.join(etc), inline = True)


    embed.set_thumbnail(url="attachment://image.gif")
    
    m = await ctx.send(file = file,embed = embed)
    
@bot.command(name = 'craft', help = 'Displays the ingredients to craft the given item')
async def craft(ctx, *args):
    item = ''
    for arg in args:
        item = item + arg + ' '
    item = item.strip().lower()

    if item.lower() == "crystal leaf earrings":
        ing = 'Crystal Leaf Earrings\nManual: Taru Totem, Naricain Jewel, Mystic Astrolabe\nTo forge: Crystal Leaf Earrings Forging MAnual and 2 Diamond'
    elif item.lower() == 'stormcaster gloves' or item.lower() == 'scg':
        ing = 'Stormcaster Gloves\nManual: Antellion Relic, Subani Ankh, Taru Totem\nTo forge: Stormcaster Gloves Forging Manual, 15 Leather, 2 Power Crystal'
    elif item.lower() == 'antellion miter':
        ing = 'Antellion Miter\nManual: Antellion Relic, Mystic Astrolabe\nTo Forge: Antellion Miter Forging Manual, 5 Gold Plate, 5 Steel Plate, 20 Screw'
    elif item.lower() == 'infinity circlet':
        ing = 'Infinity Circlet\nManual: Naricain Jewel, Subani Ankh\nTo Forge: Infinity Circlet Forging Manual, 5 Silver Plate, 1 Power Crystal, 1 Wisdom Crystal'
    elif item.lower() == 'glitter gloves':
        ing = 'Glitter Gloves\nManual: Lefay Jewel, Pharaoh''s Wrappings\nTo Forge: Glitter Gloves Forging Manual, Work Gloves, 6 Diamond, 6 Wisdom Crystal'
    elif item.lower() == 'facestompers' or item.lower() == 'fs':
        ing = 'Facestompers\nManual: Taru Totem, Stone Tiger Head\nTo Forge: Facestompers Forging Manual, 50 Steel Plate, 25 Leather, 50 Dragon Skin, 25 Screw'
    elif item.lower() == 'winkel':
        ing = 'Winkel\nManual: Lefay Jewel, Typhon Crest\nTo Forge: Winkel Forging Manual, Bow Production Manual, 50 Screw, 6 DEX Crystal, 6 Black Crystal'
    elif item.lower() == 'tiger''s fang':
        ing = 'Tiger''s Fang\nManual: Stone Tiger Head, Crystal Shard\nTo Forge: Tiger''s Fang Forging Manual, 6 Power Crystal, 6 Black Crystal'
    elif item.lower() == 'neva':
        ing = 'Neva\nManual: Pharoah''s Wrappings, Typhon Crest\nTo Forge: Neva Forging Manual, Meba, 6 Black Crystal, 6 LUK Crystal'
    elif item.lower() == 'crystal ilbi throwing-stars' or item.lower() == 'cilbi':
        ing = 'Crystal Ilbi Throwing-Stars\nManual: Crystal Shard, Naricain Jewel\nTo Forge: Crystal Ilbi Forging Manual, 1 Ilbi Throwing Star, 7 LUK Crystal, 1 Dark Crystal'
    elif item.lower() == 'bosshunter faceguard':
        ing = 'Bosshunter Faceguard\n1 Ridley''s Book of Rituals, 1 Ancient Faceguard, 1 Tengu Nose, 1 Jack O''Lantern'
    elif item.lower() == 'bosshunter gi':
        ing = 'Bosshunter Gi\n1 Ridley''s Book of Rituals, 1 Angient Gi, 1 Papulatus Curl, 1 Balrog Claw'
    elif item.lower() == 'bosshunter boots':
        ing = 'Bosshunter Boots\n1 Ridley''s Book of Rituals, 1 Ancient Boots, 1 Ergoth''s Jawbone, 1 Pianus Scale'
    elif item.lower() == 'bosshunter helm':
        ing = 'Bosshunter Helm\n1 Ridley''s Book of Rituals, 1 Ancient Helm, 1 Ergoth''s Jawbone, 1 Tengu Nose'
    elif item.lower() == 'bosshunter armor':
        ing = 'Bosshunter Armor\n1 Ridley''s Book of Rituals, 1 Ancient Armor, 1 Papulatus Curcle, 1 Pianus Scale'
    elif item.lower() == 'bosshunter greaves':
        ing = 'Bosshunter Greaves\n1 Ridley''s Book of Rituals, 1 Ancient Greaves, 1 Balrog Claw, 1 Jack O''Lantern'
    elif item.lower() == 'black phoenix shield':
        ing = 'Black Phoenix Shield\nManual: Zeta Residue, Black Versal Materia, Vorticular Gyro\nTo Forge: Black Phoenix Shield Forging Manual, 10 Mithril Plates, 2 Sapphires, 1 Dark Crystal Ore'
    elif item.lower() == 'dark shards':
        ing = 'Dark Shards\nManual: Zeta Residue, Blinking Dingbat\nTo Forge: Dark Shard Earrings Forging Manual, 10 Black Crystal Ore, 10 Power Crystal Ore'
    elif item.lower() == 'sirius cloak':
        ing = 'Sirius Cloak\nManual: Blinking Dingbat, Dark Matter, Black Versal Material\nTo Forge: Sirius Cloak Forging Manual, 5 Gold Plate, 5 Sapphire, 2 Diamond'
    elif item.lower() == 'zeta cape':
        ing = 'Zeta Cape\nManual: Dark Matter, Vorticular Gyro\nTo Forge: Zeta Cape Forging Manual, 5 Power Crystal Ore, 5 Gold Ore, 5 Opal'
    elif item.lower() == 'balanced fury' or item.lower() == 'bf' or item.lower() == 'fury':
        ing = 'Balanced Fury\n100 Black Crystals\n5 Tao of Harmony\n5 Tao of Sight\n5 Tao of Shadows\n30 Typhon Feathers\n150m mesos'
    elif item.lower() == 'crimson arcanon':
        ing = 'Crimson Arcanon\n30 Crimson Hearts\n400 Crimson Wood\nTao of Harmony\nTao of Sight\n10 Typhon Feathers\n4 Wisdom Crystals\n150k mesos'
    elif item.lower() == 'crimson arcglaive':
        ing = 'Crimson Arcglaive\n20 Crimson Hearts\n600 Crimson Wood\n4 Power Crystals\nTao of Harmony\nTao of Shadows\n40 Typhon Feathers\n150k mesos'
    elif item.lower() == 'crimson arclancer':
        ing = 'Crimson Arclancer\n10 Crimson Hearts\n300 Crimson Wood\n4 Dex Crystal\nTao of Shadows\nTao of Sight\n75 Typhon Feathers\n150k mesos'
    elif item.lower() == 'dawn raven''s beak':
        ing = 'Dawn Raven''s Beak\n20 Black Crystals\n5 Power Crystals\nRaven''s Beak\nTao of Sight\n150k mesos'
    elif item.lower() == 'dawn raven''s claw':
        ing = 'Dawn Raveon''s Claw\n20 Black Crystals\nRaven''s Claw\nTao of Sight\n10 Wisdom Crystals\n150k mesos'
    elif item.lower() == 'dawn raven''s eye':
        ing = 'Dawn Raven''s Eye\n30 Black Crystals\n5 DEX Crystals\nRaven''s Eye\nTao of Sight\n150k mesos'
    elif item.lower() == 'dawn raven''s wing':
        ing = 'Dawn Raven''s Wing\n30 Black Crystals\n10 Power Crystals\nRaven''s Wing\nTao of Sight\n150k mesos'
    elif item.lower() == 'dusk raven''s beak':
        ing = 'Dusk Raven''s Beak\n30 Black Crystals\n5 Power Crystals\nRaven''s Beak\nTao of Harmony\n150k mesos'
    elif item.lower() == 'dusk raven''s claw':
        ing = 'Dusk Raven''s Claw\n30 Black Crystals\n5 Power Crystals\nRaven''s Claw\nTao of Harmony\n150k mesos'
    elif item.lower() == 'dusk raven''s eye':
        ing = 'Dusk Raven''s Eye\n30 Black Crystals\n5 DEX Crystals\nRaven''s Eye\nTao of Harmony\n150k mesos'
    elif item.lower() == 'dusk raven''s wing':
        ing = 'Dusk Raven''s Wing\n30 Black Crystals\nRaven''s Wing\nTao of Harmony\n10 Wisdom Crystals\n150k mesos'
    elif item.lower() == 'night raven''s beak':
        ing = 'Night Raven''s Beak\n20 Black Crystals\n5 LUK Crystals\nRaven''s Beak\nTao of Shadows\n150k mesos'
    elif item.lower() == 'night raven''s claw':
        ing = 'Night Raven''s Claw\n30 Black Crystals\n10 DEX Crystals\nRaven''s Claw\nTao of Shadows\n150k mesos'
    elif item.lower() == 'night raven''s eye':
        ing = 'Night Raven''s Eye\n20 Black Crystals\n1 Dark Crystal\nRaven''s Eye\nTao of Shadows\n150k mesos'
    elif item.lower() == 'night raven''s wing':
        ing = 'Night Raven''s Wing\n30 Black Crystals\n5 DEX Crystals\nRaven''s Wing\nTao of Shadows\n150k mesos'
    elif item.lower() == 'altaire earrings':
        ing = 'Altaire Earrings\n20 Altaire Fragment\n2 Chao''s Tusk\n2 Ephenia''s Soul Shard'
    elif item.lower() == 'glittering altaire earrings':
        ing = 'Glittering Altaire Earrings\nAltaire Earrings\nStar Rock\nMoon Rock\nEllin Crystal\n100m mesos'
    elif item.lower() == 'Ephenia''s Ring':
        ing = 'Ephenia''s Ring\n20 Altaire Fragment\n10 Chao''s Tusk\n10 Ephenia''s Soul Shard'
    elif item.lower() == 'dragon carabella':
        ing = 'Dragon Carabella\nOne-Handed Sword Forging Stimulator\n1 Sparta (1h)\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon axe':
        ing = 'Dragon Axe\nOne-Handed Axe Forging Stimulator\n1 Tomahawk\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon mace':
        ing = 'Dragon Mace\nOne-Handed Blunt Weapon Forging Stimulator\n1 Battle Hammer\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon claymore':
        ing = 'Dragon Claymore\nTwo-Handed Sword Forging Stimulator\n1 The Beheader\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon battle axe':
        ing = 'Dragon Battle Axe\nTwo-Handed Axe Forging Stimulator\n1 Tavar\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon flame':
        ing = 'Dragon Flame\nTwo-Handed Mace Forging Stimulator\n1 Golden Smith Hammer\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon faltizan':
        ing = 'Dragon Faltizan\nSpear Forging Stimulator\n1 Pinaka\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon hellslayer':
        ing = 'Dragon Hellslayer\nPole Arm Forging Stimulator\n1 Zedbug\n20 Dragon Spirit\n25 Dragon Scale\n8 Power Crystal\n120,000 mesos'
    elif item.lower() == 'dragon shiner bow' or item.lower() == 'dsb':
        ing = 'Dragon Shiner Bow\nBow Production Stimulator\n1 White Nisrock\n20 Dragon Spirit\n25 Dragon Scale\n3 Power Crystal\n5 DEX Crystal\n120,000 mesos'
    elif item.lower() == 'dragon shiner cross' or item.lower() == 'dsx' or item.lower() == 'dscb' or item.lower() == 'dsxb':
        ing = 'Dragon Shiner Cross\nCrossbow Production Stimulator\n1 White Neschere\n20 Dragon Spirit\n25 Dragon Scale\n5 Power Crystal\n3 DEX Crystal\n120,000 mesos'
    elif item.lower() == 'dragon wand':
        ing = 'Dragon Wand\nWand Production Stimulator\n1 Dimon Wand\n20 Dragon Spirit\n25 Dragon Scale\n6 Wisdom Crystal\n2 LUK Crystal\n120,000 mesos'
    elif item.lower() == 'dragon staff':
        ing = 'Dragon Staff\nStaff Production Stimulator\n1 Blue Marine\n20 Dragon Spirit\n25 Dragon Scale\n6 Wisdom Crystal\n2 LUK Crystal\n120,000 mesos'
    elif item.lower() == 'dragon kanzir':
        ing = 'Dragon Kanzir\nDagger Forging Stimulator\n1 Gold Double Knife\n20 Dragon Spirit\n25 Dragon Scale\n5 Power Crystal\n3 DEX Crystal\n120,000 mesos'
    elif item.lower() == 'dragon kreda':
        ing = 'Dragon Kreda\nDagger Forging Stimulator\n1 Blood Dagger\n20 Dragon Spirit\n20 Dragon Spirit\n25 Dragon Scale\n3 DEX Crystal\n5 LUK Crystal\n120,000 mesos'
    elif item.lower() == 'dragon green sleeve' or item.lower() == 'dgs':
        ing = 'Dragon Green Sleeve\nClaw Production Stimulator\n1 Red Craven\n20 Dragon Spirit\n25 Dragon Scale\n2 DEX Crystal\n6 LUK Crystal\n120,000 mesos'
    elif item.lower() == 'dragon slash claw' or item.lower() == 'dsc':
        ing = 'Dragon Slash Claw\nKnuckle Production Stimulator\n1 King Cent\n5 Mithril Plate\n20 Dragon Spirit\n20 Dragon Scale\n3 Wisdom Crystal\n120,000 mesos'
    elif item.lower() == 'magic throwing knife' or item.lower() == 'mtk':
        ing = 'Magic Throwing Knife\nWiseman Stone: Sealed Wiseman Stone, 200 Silver Coins\nNano Plant (Omega)\nNano Plant (Sigma)\nNano Plant (Y)\n1 Ilbi Throwing-Stars\n800 Silver Coins\n500m mesos'
    elif item.lower() == 'armor-piercing bullet' or item.lower() == 'armor piercing bullet' or item.lower() == 'apb':
        ing = 'Armor-Piercing Bullet\nSaint Stone: Sealed Saint Stone, 200 Silver Coins\nNano Plant (Omega)\nNano Plant (Sigma)\nNano Plant (Y)\n1 Vital Bullet\n600 Silver Coins\n500m mesos'
    else:
        ing = 'Item not found'    
    await ctx.send(f'{ing}')

# Splits Calculator
@bot.command(name='splits', help='Calculates Splits\n !splits <price> <name of character 1> <name of character 2> <name of character3>...\n For partial splits, you can type (<percentage>) next to the character name\n Ex. !splits 1000000000 dog cat(50) rat')
async def splits(ctx, price, *argv):
    # Value of splitFactor may change if there is a partial split
    splitFactor = []
    currentMemberSplit = []
    index = 0
    partial = False
    partialSplitFactor = 1
    response = ''
    members = (argv)
    
    try:
        int(price)
    except ValueError:
        await ctx.send('Please enter a valid price, no commas')
        return

    taxedPrice = int(price)*.97
    numMembers = len(members)
    
    memberSplit = int(taxedPrice)//numMembers

    # Check for partial split
    for arg in members:
        # Parentheses in argument indicate there is a partial
        stringArg = str(arg)
        first = stringArg.find('(')
        last = stringArg.find(')')

        # Capture the partial percentage amount of split
        stringArg2 = stringArg[first+1: last]
        
        splitFactor.append(1)
        if first != -1 or last != -1:
            partial = True
            splitFactor[index]=int(stringArg2)/100
            partialSplitFactor = splitFactor[index]
        index += 1

    # Calculate each member's split
    index = 0
    for arg in members:    
        currentMemberSplit.append(int(round(taxedPrice/(numMembers-(1-partialSplitFactor))*splitFactor[index])))
        response += (f'{arg} receives {"{:,}".format(currentMemberSplit[index])} ({currentMemberSplit[index]})\n')
        index += 1

    await ctx.send(f'The total after tax is {"{:,}".format(int(round(taxedPrice)))} ({int(round(taxedPrice))}). \n\n{response}')

@bot.command(name = 'dummy', help = 'Simulates a series of dummy scrolls')
async def dummy(ctx, scrolls: int):
    passes = 0
    fails = 0
    attempts = ''
    rate = ''
    counter = 1
    # if scrolls:

    if scrolls > 1000:
        await ctx.send("Please keep the number of scrolls under 1000.")
        return
    elif scrolls < 1:
        await ctx.send("Invalid number of scrolls")
        return

    for i in range(scrolls):
        pf = round(random.random(),2)
        if pf < 0.10:
            passes = passes + 1
            attempts = attempts + str(i+1) + '   '
            if passes == scrolls/10:
                finalPass = passes
                finalAttempt = i+1
            rate = rate + str(passes) + '/' + str(counter) + '   '
            counter = 0
        else:
            fails = fails + 1
        counter = counter + 1


    if passes > 1:
        await ctx.send(file = discord.File('scrollpassed.gif'))
        await ctx.send(f'You have passed {passes} out of {scrolls} dummies.\nYou passed on attempts:    {attempts}\nYour rates are: {rate}')
        if passes >= scrolls/10:
            await ctx.send(f'You passed {finalPass} scroll(s) after {finalAttempt} tries.')
        return
    await ctx.send(file = discord.File('scrollfailed.gif'))
    await ctx.send(f'You have failed all your dummies')

# Credits
@bot.command(name = 'credits', help = 'Lists contributors of this project')
async def credits(ctx):
    credit = """
    Doo (Xves) for providing lots of details and images
    MangoSlice (Shanmango) for sharing your drop table files
    **For providing improvements and suggestions:**
    Joe (Blacephalon)
    Edi (Splats)
    John (HolyRice)
    Bun (Sharpay)
    Chris (DripBrew)
    Nicky (nickybuccc)
    Everyone else in Wiggle that helped me test my bot! Sorry cannot name you all :(
    """
    await ctx.send(credit)
bot.run(TOKEN)
