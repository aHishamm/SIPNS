# SIPNS 
I created SIPNS (Server IP Notifier System) as a simple side project to always notify me of the changing public IP address of my home server. 
The application checks the status of my server's public IP address every 45 minutes. If the IP address is updated, a notification is sent to my phone using a Telegram bot. The purpose of creating this is to always be able to ssh into my server at home, and have a record of all the changes. 

#### Installation 
```bash
conda create -n checkip python=3.10
conda activate checkip 
pip install -r requirements.txt
```

To get the bToken, open the Telegram app and search for @BotFather. /start to start the bot, and /newbot to set up the bot. You will be given an bot token.  
Then create a Telegram app by following the steps below: 
1. Log into the telegram core: https://my.telegram.org
2. Go to ‘API development tools’ and fill out the form.
3. You will get the api_id and api_hash parameters required for user authorization.  
Lastly, for the user_id, open the Telegram app and search for @userinfobot. /start to start the bot, and you will receive the user_id of your account. 
