from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("- بـدء إستخـراج كـود .", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="- رجوع .", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("- قنـاة السـورس .", url="https://t.me/x3j_xj3")],
        [
            InlineKeyboardButton("- التعـليمـات ؟! .", callback_data="help"),
            InlineKeyboardButton("- حـول البـوت .", callback_data="about")
        ],
        [InlineKeyboardButton("H𝗢𝗦𝗦𝗔𝗠࿃", url="https://t.me/H_OS_S_AM")],
    ]

    START = """
 مرحبـاً بـك عزيـزي {}

- فـي بـوت {}

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس تم انشـاء هـذا البـوت بواسطـة

- BY @H_OS_S_AM
    """

    HELP = """
** - اوامـر البــوت : **

/about - حـول البـوت
/help - التعليـمات
/start - ابـدأ 
/generate - بـدء إستخـراج جلسـه جديـده
/cancel - الغـاء
/restart - اعـادة الاستخـراج
"""

    ABOUT = """
**- حـول البـوت .** 

- بـوت استخـراج كـود تيرمكـس 
- قنـاة السـورس : @x3j_xj3

- الـمـطـور الاساسي للسورس : @FLASH_MASR .

- لغـة البـوت : بـايثـون .
    """
