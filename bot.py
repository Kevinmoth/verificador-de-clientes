import discord
import asyncio
import threading

TOKEN = 'xxx'
GUILD_ID = 988132554567745586
ROLE_ID = 988132554618044503

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

bot_ready_event = asyncio.Event()

@client.event
async def on_ready():
    print(f'[BOT] Conectado como {client.user}')
    bot_ready_event.set() 

async def asignar_rol(discord_id):
    await bot_ready_event.wait()  
    # tiempo de espera, solo en el host(en local perrea a lo loco)

    guild = client.get_guild(GUILD_ID)
    if not guild:
        print('[BOT] No se encontro el servidor')
        return

    try:
        member = await guild.fetch_member(discord_id)
        role = guild.get_role(ROLE_ID)

        if not role:
            print('[BOT] No se encontro el rol, revisa bien el id')
            return

        await member.add_roles(role)
        print(f'[BOT] Rol asignado a {member.display_name}')
        
        #Intento 9
    except Exception as e:
        print(f'[BOT] Error asignando rol (No se que paso amigo, preguntale a gpt por el siguiente error): {e}')

_loop = None

def iniciar_bot():
    global _loop

    _loop = asyncio.new_event_loop()

    def run():
        asyncio.set_event_loop(_loop)
        _loop.run_until_complete(client.start(TOKEN))

    thread = threading.Thread(target=run, name="DiscordBotThread", daemon=True)
    thread.start()

    return _loop
