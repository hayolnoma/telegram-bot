import telebot
from telebot import types

TOKEN = '7802345984:AAFAWMa5EFFFt7hK5GHkH3qpZbAcrRjkNIQ'
ADMIN_ID = 7099831932

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Xush kelibsiz")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📱 Kontaktni yuboring")
    markup.add(button)
    bot.send_message(message.chat.id, "👇 Kontaktni yuboring", reply_markup=markup)

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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbek adabiyoti", "🌍 Jahon adabiyoti")
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "✅ Rahmat! Endi menyulardan tanlang", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🕋 Islomiy kitoblar")
def islomic_books_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/tafsiri_hilol", "/jannat_vasfi", "/rizq_baraka")
    markup.add("/baxtli_hayot", "/paygambar_uyida", "/quron_qalblar")
    bot.send_message(message.chat.id, "🕌 Islomiy kitoblar bo'limi", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📈 Top 100 kitoblar")
def top100_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/top100_list", "🔙 Ortga")
    bot.send_message(message.chat.id, "📈 Top 100 kitoblar bo'limi", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🔙 Ortga")
def go_back_to_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbek adabiyoti", "🌍 Jahon adabiyoti")
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "🔙 Asosiy menyuga qaytdingiz", reply_markup=markup)

@bot.message_handler(commands=['tafsiri_hilol'])
def send_tafsir_files(message):
    files = [
        ("BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA"),
        ("BQACAgIAAxkBAAIEYGhhT-2pxKxuuTQumsVp0KP_l_LQA"),
        ("BQACAgIAAxkBAAIEYmhhT-25L2gFz48YyTwrhtTtwpTSA"),
        ("BQACAgIAAxkBAAIEY2hhT-18FD6aSW10Vd6TsxMsf-y3A"),
        ("BQACAgIAAxkBAAIEZWhhT-2MlYbnrQgx5In1k4sCVZabA"),
        ("BQACAgIAAxkBAAIEYWhhT-2qLatqmZAzUjQjutlvg-u6A"),
        ("BQACAgUAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA"),
    ]
    for file_id in files:
        bot.send_document(message.chat.id, file_id)

@bot.message_handler(commands=['jannat_vasfi'])
def send_jannat_vasfi(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA")

@bot.message_handler(commands=['rizq_baraka'])
def send_rizq_baraka(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

@bot.message_handler(commands=['istigfor_salovat'])
def send_istigfor_salovat(message):
    bot.send_document(message.chat.id, "BQACAgQAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

@bot.message_handler(commands=['baxtli_hayot'])
def send_baxtli_hayot(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA")

@bot.message_handler(commands=['paygambar_uyida'])
def send_paygambar_uyida(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA")

@bot.message_handler(commands=['quron_qalblar'])
def send_quron_qalblar(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA")

@bot.message_handler(commands=['top100_list'])
def send_top100_txt(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEX2hhT-0Nu7GnwB-_O4ynzGpdV1EvA")

print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
