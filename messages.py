import requests
import random
import os

# Get token and group ID from GitHub Secrets
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_message(message_text):
    """Send message to Telegram group"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        'chat_id': CHAT_ID,
        'text': message_text,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"✅ Message sent! Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function"""
    
    # Import messages
    from messages import MESSAGES
    
    # Use only lucy_hot category
    message_type = "lucy_hot"
    
    # Choose random message
    message = random.choice(MESSAGES[message_type])
    
    # Send exactly the message, nothing extra
    send_message(message)

if __name__ == "__main__":
    main()
