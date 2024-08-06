# ----------- Third Packages ----------
import os
from dotenv import load_dotenv
import datetime
import time
from openpyxl import Workbook
import time
import numpy as np
import asyncio
import discord
from discord.ext import commands, tasks
from urllib import parse, request
import re
# --------- End ----------------------

# -------- Internal Packages ------------
from data.personajes import enemigos as En, heroes as Hr
from data.fichaJugadores import fichaJugadores as fj
import games.first_game as fg
# --------- End -------------------------

# ------------ Numpy ----------
rutaArchivoNumpy = 'C:/Users/franc/Escritorio/Programacion/BotDiscPython/src'
accountsE = np.load(f'{rutaArchivoNumpy}/file.npy', allow_pickle='TRUE')
# -----------------------------

# ------- OpenPyXL -----------
book = Workbook()
sheet = book.active
# ----------------------------

# -------- DotEnv ----------
# load_dotenv()
# --------------------------

# .......... TOKEN ...........
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# ............................

# ------- Config CLIENT --------
client = discord.Client(intents=discord.Intents.all())
# --------------------------------

# ------- Config BOT -----
# Prefix q. or mention
bot = commands.Bot(command_prefix=commands.when_mentioned_or('q.'),description='Bot de ayuda', intents=discord.Intents.all())
# ------------------------

# ----- Global vars ------
general_channel = None
# ------------------------

# ----functions------
# Get first channel
async def get_some_channel():
    channel_list = [channel for guild in bot.guilds for channel in guild.channels if isinstance(channel,discord.channel.TextChannel)]
    principal_channel = channel_list[0]
    return principal_channel

# Get general channel
async def get_general_channel():
        global general_channel
        general_channel = [channel for guild in bot.guilds for channel in guild.text_channels if channel.name == 'general']
        if general_channel != []:
            general_channel = general_channel[0]
            return general_channel
        else:
            principal_channel = await get_some_channel()
            await principal_channel.send('Falta un chat con el nombre "general" para dar las bienvenidas')

# Welcome message
async def welcome_mention(general_channel,member):
    await general_channel.send(f"Bienvenido {member.mention} a {general_channel.mention}, espero que disfrutes tu estancia aquí. :D")

# Bye message
async def bye_message(general_channel,member):
    await general_channel.send(f'Sentimos que se haya ido {member.name}, esperamos que vuelva pronto. :c')
# -------------------

# When activate bot
@bot.event
async def on_ready():
    task_loop.start()
    # |--- Active message bot ---|
    global general_channel
    general_channel = await get_general_channel()
    if general_channel == None:
        some_channel = await get_some_channel()
        await some_channel.send('''```arm
    *-.: | Bot Timoty activo | :.-*``` ''')
    else:
        await general_channel.send('''```arm
    *-.: | Bot Timoty activo | :.-*``` ''')
    #  |--------------------------|
    # Change presence
    await bot.change_presence(activity=discord.
    CustomActivity(name='Matando el tiempo',emoji='🗡'))
    

# --------- Detect when a member join in the guild -------
@bot.event
async def on_member_join(member):
    try:
        global general_channel
        await welcome_mention(general_channel,member)
    except:
        general_channel = await get_general_channel(bot)
        if general_channel != None:
            await welcome_mention(general_channel,member)      
# ----------------------------------

# -------- Detect when a member leaves the guild -------
@bot.event
async def on_member_remove(member):
    try: 
        global general_channel
        await bye_message(general_channel,member)
    except:
        general_channel = await get_general_channel()
        if general_channel != None:
            await bye_message(general_channel,member)
# -------------------------------------------------------

# -------- Test commands --------
# Test command
@bot.hybrid_command(name='test',with_app_command=True)
async def tst(ctx):
    channel = ctx.channel
    await channel.send('complete test, congratulations')

# Its just says pong
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")

# Test commands with args
@bot.command()
async def testing(ctx, arg):
    await ctx.send(arg)

# Replace your own text
@bot.command()
async def replace(ctx):
    mensaje_remplazado = await ctx.send("Remplazando este mensaje...")
    time.sleep(2)
    await mensaje_remplazado.edit(content="El mensaje ha sido remplazado.")

# Ping in ms (time to response)
@bot.command()
async def pingms(ctx):
    before = time.monotonic()
    pong = "pong"
    response = await ctx.send(pong)
    pingA = (time.monotonic() - before)*1000
    pingB = (str(pingA).split("."))[0]
    await response.edit(content=pong + " (" + pingB + "ms)")

# Repite your words
@bot.command()
async def repite(ctx, *args):
    await ctx.send(args)

# Active when a user add reaction
@bot.event
async def on_reaction_add(reaction,user):
    if reaction.emoji == '👋':
        await reaction.message.channel.send(f'Hola {user.mention}')
#  -------------

# --- Pending ---
# A game pending
@bot.command()
async def game(ctx):...
    # if message.content.startswith('!game'): #chequea cuando el usuario escribe !game
    #     await fg.first_games(message=message,bot=bot,Hr=Hr,fj=fj,En=En,random=random)

# Test with openpyxl
@bot.command()
async def excel12(ctx, msg, numList, lettList): ...

    # sheet[f"{lettList}{numList}"] = msg

    # # excelprueba.saveDocument()

    # book.save("C:/Users/franc/Escritorio/BotDiscPython/DataBase/ExcelPrueba.xlsx")

    # await ctx.send("Listo")
# ----------------

# ----- Guild Details commands -----
# Info command
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",timestamp=datetime.datetime.now(datetime.UTC), description="Hola", color=discord.Color.dark_red())
    embed.add_field(name="El server fue creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="El dueño es", value=f"{ctx.guild.owner}")
    embed.add_field(name="Hay un total de", value=f"{ctx.guild.member_count}")
    embed.add_field(name="La región es", value=f"{None}")
    embed.add_field(name="La ID del server es", value=f"{ctx.guild.id}")
    embed.set_thumbnail(
        url="http://www.malagana.net/wp-content/uploads/2015/03/internet-explorer-windows-10.png")
    await ctx.send(embed=embed)
# ------------------------------------

# ------ Principal commands ------
# Dictionary with vars
@bot.command()
async def definicion(ctx, *, palabra):
    # Palabras y definición
    palabra = palabra.lower()
    about = "'Acerca de...', refiere a hablar sobre algo o alguien."
    I = "'Yo', habla de ti mismo."
    yes = "'Sí', aceptación o confirmación de algo."
    arigato_gozaimasu = "'Muchas gracias', forma cortez de agradecer."

    if palabra == "about":
        await ctx.send(about)

    elif palabra == "i":
        await ctx.send(I)

    elif palabra == "yes":
        await ctx.send(yes)

    elif palabra == "arigato gozaimasu" or palabra == "ありがとうございます":
        await ctx.send(arigato_gozaimasu)

    else:
        await ctx.send("La palabra es incorrecta o no existe")

# Dictionary with dict
@bot.command()
async def diccionarioT(ctx, *, palabra):
    # Palabras y definición
    palabra = palabra.lower()
    wordsdict = {
        "about": "'Acerca de...', refiere a hablar sobre algo o alguien.",
        "I": "'Yo', habla de ti mismo.",
        "yes": "'Sí', aceptación o confirmación de algo.",
        "arigato_gozaimasu": "'Muchas gracias', forma cortez de agradecer.",
    }

    if palabra == "about":
        await ctx.send(wordsdict["about"])

    elif palabra == "i":
        await ctx.send(wordsdict["I"])

    elif palabra == "yes":
        await ctx.send(wordsdict["yes"])

    elif palabra == "arigato gozaimasu" or palabra == "ありがとうございます":
        await ctx.send(wordsdict["arigato_gozaimasu"])

    else:
        await ctx.send("La palabra es incorrecta o no existe")

# Save archive (only admin)
@bot.command(name='guardar', help='Guarda todos los dict')
@commands.has_permissions(administrator=True)
async def guardar_archivos(ctx):
    np.save('file.npy', accounts)
    await ctx.send('Archivos guardados correctamente')

# See archive (only admin)
@bot.command(name='revisar', help='Ver archivos')
@commands.has_permissions(administrator=True)
async def revisar_archivos(ctx):
    new_accounts = np.load('C:/Users/franc/Escritorio/BotDiscPython/src/file.npy', allow_pickle='TRUE')
    await ctx.send(f'El archivos es {new_accounts}')
# -------------------------------------

# ------- Extra commands --------
# Search youtube video
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen(
        "http://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        'watch\?v=(.{11})', html_content.read().decode('utf-8'))
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])

# Easter egg (Only admin)
@bot.command()
@commands.has_permissions(administrator=True)
async def febrero(ctx):
    embed = discord.Embed(title="Nota de amor...")
    embed.add_field(
        name="14 de febrero. Recuerdo en mi alma que siempre fue un día que estuve solo, pero ahora tengo a la llama que prender mi amor.", value="-------")
    embed.add_field(
        name="Sabes, eres como la luna, pero en el sentido de que me iluminas por las noches más oscuras.", value="---------")
    embed.add_field(
        name="Eres la persona que aprecio como una obra de arte, no paro de contemplarte.", value="----------")
    embed.add_field(
        name="Los recuerdos y los momentos, son mi tesoro, pero sobre todo vos sos mi oro.", value="-----------")
    embed.add_field(
        name="Eres mi día favorito de la semana, o sea, eres el día que siempre espero con ansías.", value="------------")
    embed.add_field(
        name="La mecanica que me arregla cada día y pone en marcha el motor de mi corazón.", value="-------------")
    await ctx.send(embed=embed)

# Calling you command
@bot.command()
async def tag(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f" Te llaman {member.mention}, contestá")
# -------------------------------

# ------- Balance commands ------
#    ----- vars and others ----
accountsC = accountsE.tolist()

accounts = {}

permissions_accounts = []

if len(accountsC) != 0:
    accounts = accountsC
#    --------------------------
# Make accounts command
@bot.command(name='crear_cuenta', help='Creando cuenta')
async def create_account(ctx):
    if ctx.author.id not in accounts:
        accounts[ctx.author.id] = 0
        await ctx.send(f'La cuenta de {ctx.author.mention} se ha creada')
    else:
        await ctx.send(f'La cuenta de {ctx.author.mention} ya está creada')

# Make admin account command
@bot.command(name='crear_cuenta_adm', help='Creando cuenta amd')
@commands.has_permissions(administrator=True)
async def create_account_adm(ctx, user: int):
    usuario = await bot.fetch_user(user)
    if usuario.id not in accounts:
        accounts[usuario.id] = 0
        await ctx.send(f'La cuenta de {usuario.mention} se ha creada')
    else:
        await ctx.send(f'La cuenta de {usuario.mention} ya está creada')

# balance command
@bot.command(name='balance', help='Check Balance')
async def check_balance(ctx):
    if ctx.author.id in accounts:
        balance_user = accounts[ctx.author.id]
        await ctx.send(f'Su balance es de ${balance_user}')
    else:
        await ctx.send(f'Antes de realizar este comando, realice una cuenta con {str(bot.command_prefix)}crear_cuenta')

# balance check command from another user
@bot.command(name='balance_de', help='Check Balance')
async def check_balance_de(ctx, user: int):
    usuario = await bot.fetch_user(user)
    if usuario.id in accounts:
        balance_user = accounts[usuario.id]
        await ctx.send(f'Su balance es de ${balance_user}')
    else:
        await ctx.send(f'Antes de realizar este comando, realice una cuenta con {str(bot.command_prefix)}crear_cuenta')

# Add account user (only admins)
@bot.command(name='agregar_usuario', help='Agregar usuarios con permisos')
@commands.has_permissions(administrator=True)
async def admin_only(ctx, user: int):
    usuario = await bot.fetch_user(user)
    if user not in permissions_accounts:
        permissions_accounts.append(user)
        await ctx.send(f'El usuario {usuario.mention} fue agregado')
    else:
        await ctx.send(f'El usuario {usuario.mention} ya estaba agregado')

# Add money to... (admins/users with permission)
@bot.command(name='agregar_money_a', help='Agrega dinero')
async def agregar_dinero_a(ctx, user: int, mount: int):
    usuario = await bot.fetch_user(user)
    if ctx.author.id in permissions_accounts or ctx.author.guild_permissions.administrator:
        accounts[usuario.id] = accounts[usuario.id] + mount
        await ctx.send(f'El balance de {usuario.mention} ahora es de {accounts[usuario.id]}')
    else:
        await ctx.send('No tienes permisos para ejecutar este comando')

# Auto add money (admins/users with permission)
@bot.command(name='agregar_money', help='Agrega dinero')
async def agregar_dinero(ctx, mount: int):
    if ctx.author.id in permissions_accounts or ctx.author.guild_permissions.administrator:
        accounts[ctx.author.id] = accounts[ctx.author.id] + mount
        await ctx.send(f'El balance de {ctx.author.mention} ahora es de {accounts[ctx.author.id]} ')
    else:
        await ctx.send('No tienes permisos para ejecutar este comando')

# Shop catalog command
@bot.command(name='tienda', help='Abrir tienda')
async def tienda_productos(ctx):
    embed = discord.Embed(title="Catalogo tienda")

    for i, o in objetos.items():
        precio = o['precio']
        idObj = o['id']
        embed.add_field(name=f'{i} id:{idObj}', value=f'${precio}')

    await ctx.send(embed=embed)

# Buy command
@bot.command(name='comprar', help='Comprar de la tienda')
async def comprar_tienda(ctx, objId: int):
    for i, o in objetos.items():
        if o['id'] == objId:
            objEncontrado2 = o
            objEncontrado = i
    idUser = ctx.author.id
    balance = accounts[idUser]
    precioA = int(objEncontrado2['precio'])
    if accounts[idUser] >= precioA:
        accounts[idUser] = accounts[idUser] - precioA
        balance = accounts[idUser]
        await ctx.send(f'{objEncontrado} fue comprado, tu balance es de {balance}')
    else:
        if balance >= -precioA:
            accounts[idUser] = accounts[idUser] - precioA
            balance = accounts[idUser]
            await ctx.send(f'{objEncontrado} fue comprado, tu balance es de {balance}')
        else:
            await ctx.send('La compra fue rechazada, no hay fondos suficientes y ha llegado a su limite de crédito')
# ------------------------------

# ------ Others functions ------
# Save object to the shop
@tasks.loop(seconds=10)
async def task_loop():
    await bot.wait_until_ready()
    while not bot.is_closed():
        np.save('file.npy', accounts)
        await asyncio.sleep(120)
# Objects
objetos = {'Agua': {'precio': '200', 'id': 1},
           'Pan': {'precio': '300', 'id': 2}}
# ----------------------------------

# -- Run bot --
bot.run(TOKEN)
# -------------
