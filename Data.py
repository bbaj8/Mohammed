from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/7fce0278a376bf5138fe8.jpg)
اهلا {}

اهلا بك عزيزي {}


اختصاص هذا البوت تحويل الصورة الى رابط

ورفعها على التليكراف


الرجاء ارسال رابط الصورة 

ليتم تحويلها الى تليكراف
    """


    # About Message
    ABOUT = """

برمجة المطور [بايروجرام](docs.pyrogram.org)

لغة البوت [بايثون](www.python.org)

𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝙿𝚃𝙷𝙾𝙽  [𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝙿𝚃𝙷𝙾𝙽  ](https://t.me/Tepthon)

"""


    # Home Button
    home_buttons = [
        [InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝙿𝚃𝙷𝙾𝙽", url="https://t.me/Tepthon")],
        [InlineKeyboardButton("إغلاق 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 العودة إلى الصفحة الرئيسية 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝙿𝚃𝙷𝙾𝙽", url="https://t.me/Tepthon")
        ],
        [
            InlineKeyboardButton("المعلومات", callback_data="about")
        ],
        [InlineKeyboardButton("إغلاق 🔐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝙿𝚃𝙷𝙾𝙽 ", url="https://t.me/Tepthon/")],
        [InlineKeyboardButton("إغلاق 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 العودة إلى الصفحة الرئيسية 🏠", callback_data="home")]
    ]
