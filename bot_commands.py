from telegram import Update
from telegram.ext import filters
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime
from game import Game
import game
from random import randint
from time import sleep

def calcrun(userexp):
    return eval(userexp)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/calc\n/game')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Результат выражения: {calcrun(update.message.text.split(" ")[1])}')

async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка сырого текста в чате"""
    if update.message.text[0] != '/':
        # game.start()

        if game.gamestatus:
            # запущена игра
            # ход игрока
            try:
                matches = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, сколько вы берете спичек.')
                return
            if not 0 < matches < 9:
                await update.message.reply_text('можно брать только от 1 до 8 спичек')
                return
            game.action_player(matches)
            if game.check_game_state():
                await update.message.reply_text('Поздравляю вас, вы выиграли')
                game.stop()
                return
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            # ход компьютера
            message = f'Я взял {game.action_cpu()} спичек\n'
            await update.message.reply_text(message)
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            if game.check_game_state():
                message = f'Я выиграл'
                await update.message.reply_text(message)
                game.stop()
                return
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return


async def gamestart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """старт игры"""
    # game.start()
    if not game.gamestatus:
        game.start()
        message = game.help
        await update.message.reply_text(message)
        message = f'Игра началась.\nНа столе {game.heap} спичек\n'
        if randint(1, 100) > 50:
            message = 'Я хожу первый\n'
            message += f'Я взял {game.action_cpu()}\n'
            message += f'Осталось {game.heap}\nВаш ход'
            await update.message.reply_text(message)
        else:
            message = 'Ваш ход'
            await update.message.reply_text(message)

game = Game()