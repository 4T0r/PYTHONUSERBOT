from userbot import *
from PYTHONBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PYTHON"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

python = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={python})"


PM_IMG = "https://telegra.ph/file/71339ef5c1b34cffa6cb5.jpg"
pm_caption ="**Pythonẞø✞︎ 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏━━︎♠️✞t͛ẞ̸ Pythonẞø✞︎♠️━━┓**\n"
pm_caption += f"**┣🌷 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🌷 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🌷 PYTHONẞø✞︎ : {PYTHONversion}**\n"
pm_caption += f"**┣🌷 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🌷 𝙾𝚠𝚗𝚎𝚛     : [python](https://t.me/Legend_Mr_Hacker)**\n"
pm_caption += f"**┗━━━━━[♠️𝙶𝚛𝚘𝚞𝚙♠️](https://t.me/Legend_Userbot)━━━━━━━━┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/LEGEND-LX/PYTHONBOT-V9.0.8) 🔹 [📜ℓιϲєиѕє📜](https://github.com/LEGEND-LC/PYTHONBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("botalv").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'bot', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Are u alive?'
).add()
