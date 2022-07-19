#Copyright ©️ 2022 Ashmit Das. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink Bot By Ashmit Das] (https://github.com/Ashmit-Das/Telegraph-Uploader-Bot)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
اهلا {message.from_user.mention},
🔮أنا هنا لإنشاء روابط التلجراف لملفات الوسائط الخاصة بك.

👨🏼‍💻ما عليك سوى إرسال ملف وسائط صالح مباشرة إلى هذه الدردشة.
♻️انواع الملفات الصالحه هي:- 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

🌐لأنشاء الروابط في المجموعات,اضفني لمجموعه خارقه اي عامه وارسل الامر /tl ردا علي ملف وسائط صالح.

🏠 | [قناة البوت الاولي](https://t.me/Big1_Bang1)
🏠 | [قناة البوت الثانية](https://t.me/B_O_S_T_A_T_0)
🏠 | [قناة البوت الثالثه](https://t.me/A_G_R_0)
🥳 | [المطور](https://t.me/G5_F1)            
"""
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("يتم المعالجه...")
        async def progress(current, total):
            await text.edit_text(f"📥 يتم التحميل {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 يتم الرفع!")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | رابط التليجراف**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | Kuch Garbar Huyi Hai Really 😢**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("يتم المعالجه...")
        async def progress(current, total):
            await text.edit_text(f"📥 يتم التحميل {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 يتم الرفع!")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | رابط التليجراف**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | Kuch Garbar Huyi Hai Really 😢**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("تم تشغيل البوت روح اضغط ستارت!")
teletips.run()

#Copyright ©️ 2022 Ashmit Das. All Rights Reserved
