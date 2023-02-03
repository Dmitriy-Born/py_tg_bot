from telegram import Update
from telegram.ext import filters
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import bot_commands as bc




app = ApplicationBuilder().token("5724308043:AAE1xDePWbG4LQegS3YBrMr3dAPPHcRUavU").build()

app.add_handler(CommandHandler("start", bc.start_command))
app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("calc", bc.calc_command))
app.add_handler(CommandHandler("game", bc.gamestart))
app.add_handler(CommandHandler("hello", bc.hi_command))
app.add_handler(MessageHandler(None, bc.message_processing))

print('start_server')
app.run_polling()