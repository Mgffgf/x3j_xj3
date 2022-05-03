import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringSessionBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer("يرجى ملاحظة أن النوع الجديد من جلسات السلسلة قد لا يعمل في جميع الروبوتات ، أي فقط الروبوتات التي تم تحديثها إلى Pyrogram V2 ستعمل!", show_alert=True)
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            # elif query == "pyrogram_bot":
            #     await callback_query.answer("Please note that this bot session will be of pyrogram v2", show_alert=True)
            #     await generate_session(bot, callback_query.message, is_bot=True)
            # elif query == "telethon_bot":
            #     await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "- عـذراً حدث خطأ ! \n\n**خطأ !** : {} " \
            "\n\n- يرجى ابلاغي اذا كان هناك خطأ @H_OS_S_AM " \
            "معلومات حساسة وأنت إذا كنت تريد الإبلاغ عن هذا كـ" \
            "لم يتم تسجيل رسالة الخطأ هذه بواسطتنا!"