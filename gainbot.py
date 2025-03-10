import os
import telebot

# Récupérer le token depuis une variable d'environnement
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Vérifier si le token est bien chargé
if not TOKEN:
    raise ValueError("❌ Erreur : Le token du bot n'est pas défini ! Assurez-vous d'avoir configuré la variable d'environnement.")

bot = telebot.TeleBot(TOKEN)

# Commande /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bienvenue sur GainBot ! Tape /help pour voir les options.")

# Commande /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "📌 **Commandes disponibles :**\n"
        "/start - Démarrer le bot\n"
        "/premium - S'abonner à GainBot Premium\n"
        "/help - Obtenir de l'aide",
        parse_mode="Markdown"
    )

# Commande /premium
@bot.message_handler(commands=['premium'])
def premium(message):
    bot.send_message(
        message.chat.id,
        "💎 **Pour accéder à GainBot Premium, clique ici :**\n\n"
        "[Paiement sécurisé via Mollie](https://pay.mollie.com/gainbot-premium)",
        parse_mode="Markdown"
    )

print("✅ GainBot est en ligne...")

bot.polling()
