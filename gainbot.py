import telebot

# 🔹 Remplace par ton Token API donné par BotFather
TOKEN = "7847892552:AAFg8UMNV2KJ5_dK2E1c5o2ln-rjq16Bc_E"
bot = telebot.TeleBot(TOKEN)

# 📌 Commande /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🚀 Bienvenue sur GainBot ! Tape /help pour voir les options.")

# 📌 Commande /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "📌 Commandes disponibles :\n"
                                      "/start - Démarrer le bot\n"
                                      "/premium - S’abonner à GainBot Premium\n"
                                      "/help - Obtenir de l’aide")

# 📌 Commande /premium (renvoie vers le paiement Mollie)
@bot.message_handler(commands=['premium'])
def premium(message):
    bot.send_message(message.chat.id, "💳 **Pour accéder à GainBot Premium, clique ici :**\n"
                                      "🔗 [Paiement sécurisé via Mollie](https://pay.mollie.com/gainbot-premium)",
                     parse_mode="Markdown")

# 🔥 Lancer le bot
print("🚀 GainBot est en ligne...")
bot.polling()
