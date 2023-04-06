from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient
import threading, os, telebot
import public_ip as ip 
import streamlit as st 
from datetime import datetime 
import time
from dotenv import load_dotenv
load_dotenv()
#loading the environment variables 
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
bToken = os.getenv("BOT_TOKEN")
user_id = os.getenv("USER_ID")
def run_periodically(): 
    while True: 
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
        print("New server IP address: ",ip.get())
        time.sleep(28800.0) #sleep for 8 hours 
run_periodically()