from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

__MODULE__ = "sᴘᴏᴛɪғʏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴏᴛɪғʏ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}spotify</code> judul lagu
⊶ Mendownload Music</b></blockquote>
"""

BOT_TARGET = "Song_vkm_bot"

@Client.on_message(filters.command("spotify", prefixes=".") & filters.me)
async def spotify_search(client: Client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("⚠️ Gunakan format: `.spotify <judul lagu>`")

    status = await message.reply("🎶 Mencari lagu...")

    # 1. Kirim perintah ke @Song_vkm_bot
    await client.send_message(BOT_TARGET, f"/start {query}")

    # 2. Tunggu balasan dengan tombol
    try:
        response = await client.listen(BOT_TARGET, timeout=15)
    except asyncio.TimeoutError:
        return await status.edit("❌ Bot tidak merespons. Coba lagi.")

    if not response.reply_markup:
        return await status.edit("❌ Tidak ada hasil ditemukan.")

    # 3. Klik tombol pertama
    try:
        first_button = response.reply_markup.inline_keyboard[0][0]
        await response.click(first_button.text)
    except Exception as e:
        return await status.edit(f"⚠️ Gagal klik tombol: {e}")

    # 4. Tunggu musik dikirim
    try:
        song = await client.listen(BOT_TARGET, timeout=30)
    except asyncio.TimeoutError:
        return await status.edit("❌ Lagu tidak terkirim.")

    if not song.audio:
        return await status.edit("❌ Respon bukan audio.")

    # 5. Forward musik ke chat user
    await song.copy(message.chat.id, caption=f"🎵 Hasil pencarian: <b>{query}</b>")
    await status.delete()
