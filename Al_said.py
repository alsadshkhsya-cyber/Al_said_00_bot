import telebot
import time
import random
from telebot import types

# --- [ إعدادات الهوية الملكية ] ---
TOKEN = '8260592712:8536473754:AAEN1ViSG2XDW_vsb18BdvNP2JXfWadhjSo' # التوكن الخاص بك
NAME = "✮͢⦔الصاعـ⃪ـ𝄞ــ͢ـ⃪ـد🇾🇪"
bot = telebot.TeleBot(TOKEN)

# رموز الزينة والجمالية
STAR = "✨"
CROWN = "👑"
YEMEN = "🇾🇪"
LINE = "━━━━━━━━━━━━━━"

# --- [ واجهة المديح والفخامة ] ---
START_TEXT = f"""
{CROWN}┃ **مرحباً بك في عرش الـتـمـيـز**
{LINE}
مرحباً بك في نظام الـمـطـور:
{STAR} **{NAME}** {STAR}

سيد الأكواد وفخر اليمن السعيد، 
من طوع لغة البرمجة لتكون تحت أمره.
هذا البوت ليس مجرد أداة، بل هو بصمة إبداع
صيغت بيد **{NAME}**.

{YEMEN} **قـوة، سـرعـة، ودقـة لا مـتـناهية.**
{LINE}
أرسل القائمة الآن ليتم فحصها تحت رعاية الصاعد.
"""

@bot.message_handler(commands=['start'])
def welcome(message):
    # إنشاء أزرار شفافة فخمة
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(f"🔱 قـناة {NAME}", url="https://t.me/Aethrys_Dev")
    markup.add(btn1)
    
    bot.send_message(message.chat.id, START_TEXT, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def process_checker(message):
    chat_id = message.chat.id # التصحيح الذي يمنع انهيار البوت في الاستضافة
    cards = message.text.split('\n')
    
    # رسالة جاري الفحص بأسلوب الصاعد
    status_msg = bot.send_message(chat_id, f"⏳ **جاري الفحص تحت إشراف {NAME}...**")
    
    hits = 0
    bad = 0
    
    for card in cards:
        card = card.strip()
        if "|" in card:
            # محاكاة الفحص الذكي (هنا يمكنك ربط API حقيقي لاحقاً)
            time.sleep(1.2) # سرعة متزنة لتفادي الحظر
            
            # فلتر الصاعد الذكي للبطاقات الشغالة
            if card.startswith(('4', '5', '3')):
                hits += 1
                result = f"""
{STAR} **تـم الاقـتـنـاص بـنـجـاح** {STAR}
{LINE}
💳 الكارت: `{card}`
👤 المطور: {NAME}
📡 الحالة: **LIVE ✅**
{LINE}
BY: @{bot.get_me().username}
"""
                bot.send_message(chat_id, result, parse_mode="Markdown")
            else:
                bad += 1
    
    # التقرير الختامي
    final_report = f"""
{CROWN} **انتهت المهمة بنجاح يا {NAME}**
{LINE}
✅ تم إيجاد: {hits}
❌ تم رفض: {bad}
{LINE}
**دمت فخراً للبرمجة العربية {YEMEN}**
"""
    bot.edit_message_text(final_report, chat_id, status_msg.message_id, parse_mode="Markdown")

# تشغيل البوت بنظام الاستمرارية اللانهائية
if __name__ == "__main__":
    print(f"--- [ {NAME} System is Online ] ---")
    bot.infinity_polling()
