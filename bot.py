import telebot
from telebot import types

TOKEN = '7802345984:AAFAWMa5EFFFt7hK5GHkH3qpZbAcrRjkNIQ'  # O'zingizning tokeningiz
ADMIN_ID = 7099831932  # Adminning IDsi

bot = telebot.TeleBot(TOKEN)

# Webhookni o'chirish
bot.remove_webhook()

# /start komandasini qo'shish
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Xush kelibsiz!\n\nBotdan foydalanish uchun iltimos kontakt yuboring.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("📱 Kontaktni yuborish", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, "👇 Kontaktni yuborish uchun tugmani bosing:", reply_markup=markup)

# Kontakt kelganda
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user = message.contact
    info = (
        f"📥 Yangi foydalanuvchi:\n"
        f"👤 Ismi: {user.first_name}\n"
        f"📞 Tel: {user.phone_number}\n"
        f"🆔 ID: {user.user_id}"
    )
    bot.send_message(ADMIN_ID, info)

    # Asosiy menyu
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbek adabiyoti", "🌍 Jahon adabiyoti")
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "✅ Rahmat! Endi menyudan foydalanishingiz mumkin:", reply_markup=markup)

# Islomiy kitoblar menyusi
@bot.message_handler(func=lambda m: m.text == "🕋 Islomiy kitoblar")
def islomic_books_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/tafsiri_hilol", "/jannat_vasfi", "/rizq_baraka", "/istigfor_salovat")
    markup.add("/baxtli_hayot", "/paygambar_uyida", "/quron_qalblar", "🔙 Ortga")
    bot.send_message(message.chat.id, "🕌 Islomiy kitoblar komandalarini tanlang:", reply_markup=markup)

# Top 100 kitoblar menyusi
@bot.message_handler(func=lambda m: m.text == "📈 Top 100 kitoblar")
def top100_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/top100_list", "🔙 Ortga")
    bot.send_message(message.chat.id, "📈 Top 100 kitoblar ro‘yxati:", reply_markup=markup)

# Ortga tugmasi ishlovchisi
@bot.message_handler(func=lambda message: message.text == "🔙 Ortga")
def go_back_to_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbek adabiyoti", "🌍 Jahon adabiyoti")
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "🔙 Asosiy menyuga qaytdingiz:", reply_markup=markup)

# Islomiy kitoblar komandalar
@bot.message_handler(commands=['tafsiri_hilol'])
def send_tafsir_files(message):
    files = [
        ("BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSAAJeBAACCpAhS_oy_R6wll9BNgQ", "📘 Tafsiri Hilol - 1-juz"),
        ("BQACAgIAAxkBAAIEYGhhT-2pxKxuuTQumsVp0KP_l_LQAALQAwACtAogSyLG-9q1zrPvNgQ", "📘 Tafsiri Hilol - 2-juz"),
        ("BQACAgIAAxkBAAIEYmhhT-25L2gFz48YyTwrhtTtwpTSAALRAwACtAogS0rL0RNVgIo5NgQ", "📘 Tafsiri Hilol - 3-juz"),
        ("BQACAgIAAxkBAAIEY2hhT-18FD6aSW10Vd6TsxMsf-y3AALTAwACtAogS3FbbcxdqK38NgQ", "📘 Tafsiri Hilol - 5-juz"),
        ("BQACAgIAAxkBAAIEZWhhT-2MlYbnrQgx5In1k4sCVZabAALUAwACtAogSyS1KS-saNZ0NgQ", "📘 Tafsiri Hilol - 6-juz"),
        ("BQACAgIAAxkBAAIEYWhhT-2qLatqmZAzUjQjutlvg-u6AAK1AANNvlhJkt77CiIxPLM2BA", "📱 Tafsiri Hilol APK (1)"),
        ("BQACAgUAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvAAJHAQAC60eAVPyWEhX4ShJSNgQ", "📱 Tafsiri Hilol APK (2)")
    ]
    for file_id, caption in files:
        bot.send_document(message.chat.id, file_id, caption=caption)

@bot.message_handler(commands=['jannat_vasfi'])
def send_jannat_vasfi(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEfWhhUTzgOIujTxegSrpkXCD2pGdkAALJBAACTWYwSM_P4xiT9wpINgQ", caption="🌴 Jannat vasfi")

@bot.message_handler(commands=['rizq_baraka'])
def send_rizq_baraka(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEf2hhUUbEB-0QmJFY3JUdVBiepPxwAAJnAwACqAfwSFtF_vXwLl7rNgQ", caption="💰 Keng rizq va baraka omillari")

@bot.message_handler(commands=['istigfor_salovat'])
def send_istigfor_salovat(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIEgWhhUVcB9yUnf9cAAaXZxz7lUlwIKgACcgkAAnbXeVBoozMqw0wJ1jYE", caption="🕊 Istigfor va Salovotlar")

@bot.message_handler(commands=['baxtli_hayot'])
def send_baxtli_hayot(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEg2hhUVdo5HZMsA1rIYxjIZdsVeQgAAJIAgACpPxQSAh-WOpwtsnrNgQ", caption="🌟 Baxtli hayot sari")

@bot.message_handler(commands=['paygambar_uyida'])
def send_paygambar_uyida(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEhGhhUVf8cTl-dWj_JQJAc4G3Gv-6AALRBgAC5Jm4SOFHSLdNL2EwNgQ", caption="🏠 Payg‘ambar uyida bir kun")

@bot.message_handler(commands=['quron_qalblar'])
def send_quron_qalblar(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEgmhhUVfhd7PXMVKEeok3o5GX33_nAAJZAQACWs0pSDNEENbNsOcONgQ", caption="📖 Qur'on – qalblar shifosi")

@bot.message_handler(commands=['top100_list'])
def send_top100_txt(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEiWhhUfd7rTKSMbBdwu_TIri17ZdJAALfAgACb4_QSNDwECbXsp_fNgQ", caption="📋 Top 100 kitob ro‘yxati")

# Pollingni ishga tushurish
print("🤖 Bot ishga tushdi... Kutyapman...")
bot.infinity_polling()
