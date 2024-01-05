from telegram import Update
from telegram import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import wikipedia
import smtplib
from email.mime.text import MIMEText

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Assalomu alaykum! Wikipedia ma\'lumotlarini olish uchun /get_info buyrug\'ini yuboring.')

def get_info(update: Update, context: CallbackContext) -> None:
    query = context.args
    if not query:
        update.message.reply_text('Iltimos, qidiruv so\'rozini yuboring. Masalan: /get_info Car')
    else:
        result = wikipedia.summary(" ".join(query), sentences=2)
        send_email("mamajonovibrokhimjon@gmail.com", "Wikipedia Info", result)
        update.message.reply_text('Ma\'lumot jo\'natildi.')

def send_email(to_address, subject, body):
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "fatxullohibrohim@gmail.com"
    smtp_password = "ismoil_999"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = to_address

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_address, msg.as_string())

def main() -> None:
    updater = Updater("5754196545:AAH-iJtTHHFhdq5BnVqKhVPSzbx_H9zVa5o")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_info", get_info))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()