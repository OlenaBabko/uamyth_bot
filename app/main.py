
import logging

from config.env import get_settings
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

from llama_index import load_index_from_storage
from llama_index.response.schema import Response
from llama_index.storage import StorageContext
env = get_settings()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# index = load_index_from_storage(storage_context)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    menu_buttons = [
    ["Цитата дня", "Метафорична карта"],
    ["Твоє сузір'я", "Руна дня"],
    ["Міфологічна істота на день", "Рослини"]
    ]
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)

    await update.message.reply_html(
        rf"""Ласкаво просимо до нашого міфологічного світу!
Я - ваш вірний чат-бот, готовий допомогти вам розкрити таємниці української міфології та культури. 
Задайте питання, отримайте натхнення, збагачуйте свої знання про українські легенди та магію рун. 
Дозвольте мені бути вашим провідником у світі символіки та магії!
Готові розпочати захопливу подорож? 
Просто оберіть розділ, який вас цікавить!
""",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # reply = index.as_query_engine().query(update.message.text)
    reply = ""
    await update.message.reply_text(reply.response)


def main() -> None:
    application = Application.builder().token(env.BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


async def handle_menu_choice(update: Update, context: CallbackContext) -> None:
    selected_option = update.message.text

    # Define functions for each menu option
    if selected_option == "Цитата дня":
        await send_quote_of_the_day(update)
    elif selected_option == "Метафорична карта":
        await send_metaphorical_map(update)
    elif selected_option == "Твоє сузір'я":
        await send_constellation_details(update)
    elif selected_option == "Руна дня":
        await send_rune_of_the_day(update)
    elif selected_option == "Міфологічна істота на день":
        await send_mythological_creature(update)
    elif selected_option == "Рослини":
        await send_plants_info(update)
    elif selected_option == "Назад":
        await start(update, context)  # Call the start function to display the main menu again.
    else:
        await update.message.reply_text("Оберіть дію з вказаного меню.")

# Define functions for each menu option
async def send_quote_of_the_day(update: Update):
    await update.message.reply_text("Відкрийте для себе захоплюючі фрази з віршів та творів великих українських письменників і поетів, які містять міфологічні мотиви. Ці цитати надихнуть вас, допоможуть знайти нові думки та зосередитися на важливих аспектах життя.")

async def send_metaphorical_map(update: Update):
    await update.message.reply_text("Запитайте у чат-бота питання, що хвилює вас, і отримайте метафоричну карту, у якій кожна карта має свою символіку, пов'язану з українськими міфами та легендами. Вона допоможе краще зрозуміти ситуацію, відкрити нові погляди та знайти натхнення для подальших кроків.")

async def send_constellation_details(update: Update):
    await update.message.reply_text("Дізнайтеся свій унікальний гороскоп, створений на основі українських міфів та архетипів. Цей гороскоп допоможе вам розкрити свій потенціал, зосередитися на головному та знайти гармонію з навколишнім світом.")

async def send_rune_of_the_day(update: Update):
    await update.message.reply_text("Отримайте свою руну на день, яка буде символізувати ключові якості або теми, що впливають на ваш день. Вона допоможе вам зосередитися на важливих аспектах, зробити вірні вибори та знайти рішення у складних ситуаціях.")

async def send_mythological_creature(update: Update):
    await update.message.reply_text("Отримайте підтримку від міфологічної істоти, яка буде супроводжувати вас протягом усього дня. Ця істота наділена магічною силою, яка може допомогти вам у складних ситуаціях та надати вам натхнення для досягнення ваших цілей.")

async def send_plants_info(update: Update):
    await update.message.reply_text("...")  # Replace ... with information about plants.

if __name__ == "__main__":
    main()
    