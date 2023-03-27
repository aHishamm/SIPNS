import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient
import threading, os 
import public_ip as ip 
from datetime import datetime 
from dotenv import load_dotenv
load_dotenv()
#loading the environment variables 
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
bToken = os.getenv("BOT_TOKEN")
user_id = os.getenv("USER_ID")

current_add = ''  
def run_periodically(): 
    global current_add
    threading.Timer(2700.0,run_periodically).start() #runs every 45 minutes/2700 seconds
    if current_add != ip.get(): 
        current_add = ip.get() 
        #connecting to Telegram
        client = TelegramClient('session',api_id,api_hash)
        client.connect() 
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone_number,input("Please enter the code: "))
        try: 
            receiver = InputPeerUser(int(user_id),0)
            client.send_message(receiver,"New server IP address: "+ip.get(),parse_mode='html')
        except Exception as e: 
            print(e) 
        client.disconnect() 
        print("Message Sent")
        print("New server IP address: ",current_add)
run_periodically()