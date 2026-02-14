import requests
import random
import os
import sys

# Get token and group IDs from GitHub Secrets
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GROUP1_ID = os.environ.get('GROUP1_ID')  # آیدی گروه اول
GROUP2_ID = os.environ.get('GROUP2_ID')  # آیدی گروه دوم

# ببین کدوم گروه قراره پیام بگیره (از ورودی می‌گیریم)
# توی workflow مشخص می‌کنیم که کدوم گروه اجرا بشه
import sys
target_group = sys.argv[1] if len(sys.argv) > 1 else "group1"

def send_message(chat_id, message_text):
    """Send message to specific Telegram group"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': message_text,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"✅ Message sent to {chat_id}! Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function"""
    
    # بر اساس گروه هدف، فایل پیام مناسب رو ایمپورت کن
    if target_group == "group1":
        from messages_group1 import MESSAGES
        chat_id = GROUP1_ID
        print("📨 Sending to Group 1")
    else:
        from messages_group2 import MESSAGES
        chat_id = GROUP2_ID
        print("📨 Sending to Group 2")
    
    # از دسته lucy_hot استفاده کن
    message_type = "lucy_hot"
    
    # یه پیام تصادفی انتخاب کن
    message = random.choice(MESSAGES[message_type])
    
    # یه رکورد بذار که بدونیم کدوم پیام رفت (اختیاری)
    print(f"📝 Selected message: {message[:30]}...")
    
    # بفرست
    send_message(chat_id, message)

if __name__ == "__main__":
    main()
