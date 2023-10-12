import os
import logging
import random
from sorular import D_SORU, C_SORU
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = os.getenv("OWNER_API_ID", "24092943") # KARIŞMAYIN
API_HASH = os.getenv("OWNER_API_HASH", "5e8dd78f2592f39e139e3d803db522c4") # KARIŞMAYIN
B_TOKEN = os.getenv("BOT_TOKEN", "") # BOT TOKENİ GİRİN
OWNER_ID = os.getenv("OWNER_ID", "").split() # BOT SAHİP İD'Sİ GİRİN .
OWNER_ID.append() # BOT SAHİP İD'Sİ GİRİN . 

MOD = None

logging.basicConfig(level=logging.INFO)

K_G = Client(
	"Pyrogram Bot",
	bot_token=B_TOKEN,
	api_id=API_ID,
	api_hash=API_HASH
	)

# START KOMUT BUTONLARI
def button():
	BUTTON=[[InlineKeyboardButton(text="➕ 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 ➕",url="https://t.me/EpikTestBot?startgroup=a")]]
	BUTTON+=[[InlineKeyboardButton(text="👤 𝖮𝗐𝗇𝖾𝗋",url="https://t.me/EpikOwner")]]
	return InlineKeyboardMarkup(BUTTON)


# DC KOMUTU İCİN BUTTONLAR
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="📕 Doğruluk", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="📓 Cesaret", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

# DC KOMUTU
@K_G.on_message(filters.command("dc"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="**{}\n👻 Dostum, bir seçim yap .\n\n📕 Doğruluk Mu ?\n📓 Cesaret Mi ?**".format(user.mention),
		reply_markup=d_or_c(user.id)
		)


                # CESARET SORUSU
		if c_q_d == "c_data":
			await callback_query.answer(text="📓 Cesaret Sorusu İstedin .", show_alert=False)


K_G.run() # Botumuzu Calıştıralım :)
