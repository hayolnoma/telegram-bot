import telebot
from telebot import types

TOKEN = '7802345984:AAFAWMa5EFFFt7hK5GHkH3qpZbAcrRjkNIQ'
ADMIN_ID = 7099831932

bot = telebot.TeleBot(TOKEN)

# Start komanda
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Xush kelibsiz")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📱 Kontaktni yuborish")
    markup.add(button)
    bot.send_message(message.chat.id, "👇 Kontaktni yuboring", reply_markup=markup)

# Foydalanuvchi kontaktini qabul qilish
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

# Islomiy kitoblar
@bot.message_handler(func=lambda m: m.text == "🕋 Islomiy kitoblar")
def islomic_books_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/tafsiri_hilol", "/jannat_vasfi", "/rizq_baraka")
    markup.add("/baxtli_hayot", "/paygambar_uyida", "/quron_qalblar")
    bot.send_message(message.chat.id, "🕌 Islomiy kitoblar bo'limi", reply_markup=markup)

# Top 100 kitoblar
@bot.message_handler(func=lambda m: m.text == "📈 Top 100 kitoblar")
def top100_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/top100_list", "🔙 Ortga")
    bot.send_message(message.chat.id, "📈 Top 100 kitoblar bo'limi", reply_markup=markup)

# Asosiy menyuga qaytish
@bot.message_handler(func=lambda message: message.text == "🔙 Ortga")
def go_back_to_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbek adabiyoti", "🌍 Jahon adabiyoti")
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "🔙 Asosiy menyuga qaytdingiz", reply_markup=markup)

# Tafsirlar
@bot.message_handler(commands=['tafsiri_hilol'])
def send_tafsir_files(message):
    files = [
        ("BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA"),
        ("BQACAgIAAxkBAAIEYGhhT-2pxKxuuTQumsVp0KP_l_LQA"),
        ("BQACAgIAAxkBAAIEYmhhT-25L2gFz48YyTwrhtTtwpTSA"),
        # Yana fayllarni qo‘shish
    ]
    for file_id in files:
        bot.send_document(message.chat.id, file_id)

# Jannat vasfi
@bot.message_handler(commands=['jannat_vasfi'])
def send_jannat_vasfi(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

# Rizq baraka
@bot.message_handler(commands=['rizq_baraka'])
def send_rizq_baraka(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

# Baxtli hayot
@bot.message_handler(commands=['baxtli_hayot'])
def send_baxtli_hayot(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

# Top 100 kitoblar ro'yxati
@bot.message_handler(commands=['top100_list'])
def send_top100_txt(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIEZGhhT-3LusRuv5bVnt07OBxQq7vSA")

# Ping xabari (botni sinash)
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id, "Pong!")

# Adminlarga xabar yuborish
@bot.message_handler(commands=['admin_ping'])
def admin_ping(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "👋 Salom admin! Bot ishlayapti.")
    else:
        bot.send_message(message.chat.id, "Siz admin emassiz.")

# Bot ishga tushdi
print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
