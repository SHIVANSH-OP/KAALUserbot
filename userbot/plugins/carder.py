import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from kaalBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from kaalBOT import CmdHelp, bot as W2HBOT


@kaalBOT.on(admin_cmd("gencc$"))
@kaalBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(kaalevent):
    if kaalevent.fwd_from:
        return
    kaalcc = Faker()
    kaalname = kaalcc.name()
    kaaladre = kaalcc.address()
    kaalcard = kaalcc.credit_card_full()
    
    await edit_or_reply(kaalevent, f"__**👤 NAME :- **__\n`{kaalname}`\n\n__**🏡 ADDRESS :- **__\n`{kaaladre}`\n\n__**💸 CARD :- **__\n`{kaalcard}`")
    

@kaalBOT.on(admin_cmd(pattern="bin ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/bin {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@kaalBOT.on(admin_cmd(pattern="vbv ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="vbv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/vbv {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
    
    
@kaalBOT.on(admin_cmd(pattern="key ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="key ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/key {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
 
  
@kaalBOT.on(admin_cmd(pattern="iban ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/iban {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
@kaalBOT.on(admin_cmd(pattern="ccheck ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="ccheck ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/ss {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             
             
@kaalBOT.on(admin_cmd(pattern="ccbin ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="ccbin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    kaal_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{kaal_input}`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/gen {kaal_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
CmdHelp("carder").add_command(
  "gencc", None, "Generates fake cc..."
).add_command(
  "ccheck", "<query>", "Checks that the given cc is live or not"
).add_command(
  "iban", "<query>", "Checks that the given IBAN ID is live or not"
).add_command(
  "key", "<query>", "Checks the status of probided key"
).add_command(
  "vbv", "<query>", "Checks the vbv status of given card"
).add_command(
  "bin", "<query>", "Checks that the given bin is valid or not"
).add_command(
  "ccbin", "<bin>", "Generates CC from the given bin."
).add()
