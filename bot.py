import requests
import random
import os
from datetime import datetime

# گرفتن توکن و آیدی گروه از Secrets گیت‌هاب
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# ایموجی‌های مختلف برای هر موقع از روز
MORNING_EMOJIS = ["🌅", "🌞", "☀️", "🌸", "🌺", "🌼"]
AFTERNOON_EMOJIS = ["☕️", "🍃", "🌿", "🍵", "✨", "💫"]
EVENING_EMOJIS = ["🌆", "🌇", "🌙", "⭐️", "🌟", "💫"]
NIGHT_EMOJIS = ["🌜", "🌛", "💤", "😴", "⭐️", "✨"]

# اسم‌های قشنگ برای فرستنده (این رو بات نمی‌تونه تغییر بده، ولی تو پیام می‌نویسیم)
SENDER_NAMES = ["🌸 الناز", "🌺 سارا", "💐 زهرا", "🌷 فاطمه", "🌸 مریم", "🌼 نیلوفر"]

def get_time_based_emoji():
    """بر اساس ساعت روز، ایموجی مناسب رو برمی‌گردونه"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return random.choice(MORNING_EMOJIS)
    elif 12 <= hour < 17:
        return random.choice(AFTERNOON_EMOJIS)
    elif 17 <= hour < 21:
        return random.choice(EVENING_EMOJIS)
    else:
        return random.choice(NIGHT_EMOJIS)

def send_message(message_text):
    """ارسال پیام به گروه تلگرام"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        'chat_id': CHAT_ID,
        'text': message_text,
        'parse_mode': 'HTML'  # برای استفاده از HTML توی پیام
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"✅ پیام ارسال شد! وضعیت: {response.status_code}")
        print(f"📨 متن پیام: {message_text[:50]}...")
        return True
    except Exception as e:
        print(f"❌ خطا در ارسال: {e}")
        return False

def main():
    """تابع اصلی که اجرا میشه"""
    
    # ایمپورت کردن لیست پیام‌ها از فایل جداگانه
    from messages import MESSAGES
    
    # انتخاب یه اسم تصادفی
    sender_name = random.choice(SENDER_NAMES)
    
    # انتخاب یه ایموجی بر اساس ساعت
    time_emoji = get_time_based_emoji()
    
    # ساعت فعلی
    current_time = datetime.now().strftime("%H:%M")
    
    # انتخاب یه پیام تصادفی
    message_type = random.choice(list(MESSAGES.keys()))
    message = random.choice(MESSAGES[message_type])
    
    # ساخت متن نهایی
    final_message = f"{time_emoji} <b>{sender_name}</b>\n"
    final_message += f"🕐 {current_time}\n\n"
    final_message += f"{message}\n\n"
    final_message += f"✨ {random.choice(['روز قشنگ', 'شب آروم', 'عصر دلنشین', 'صبح زیبا'])}"
    
    # ارسال پیام
    send_message(final_message)

if __name__ == "__main__":
    main()