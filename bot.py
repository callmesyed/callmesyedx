from bard import BardBot
from telebot import TeleBot

TOKEN = '6180815307:AAH-JHu3G_Kpa0d11C9esMBgxZddduhm3h0'
SECURE_1PSID = 'agipmrhs2HdYjGRf1sZJdvMt1pEq4wJiPsJdzWqqtLSAzP78b4uGpwdvrPOuo7FOrXvJUg.'
SECURE_1PSIDTS = 'sidts-CjIBSAxbGc0PFyegSFQFtkM5VwePahmX-y46o6hRq-lFvXorip0Aw7dgG-itfeaPS1dbfBAA'

bard = BardBot(SECURE_1PSID, SECURE_1PSIDTS)
bot = TeleBot(TOKEN)

def extract_arg(arg):
    return arg.split()[1:]

def train():
    with open("extra.txt") as file:
        extra = file.read()

    return extra

bard.ask(train())
print("Training done...")

@bot.message_handler(commands=["bot"])
def handle_ask(message):
    question = " ".join(extract_arg(message.text))

    thinking_message = bot.reply_to(message, "Thinking...")
    answer = bard.ask(question).get("content")
    bot.edit_message_text(chat_id=message.chat.id, message_id=thinking_message.message_id, text=answer)

if __name__ == "__main__":
    bot.infinity_polling()