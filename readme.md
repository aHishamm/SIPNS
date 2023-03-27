# SIPNS 
I created SIPNS (Server IP Notifier System) as a simple side project to always notify me of the changing public IP address of my home server. 
The application checks the status of my server's public IP address every 12 hours. If the IP address is updated, a notification is sent to my phone using a Telegram bot. The purpose of creating this is to always be able to ssh into my server at home, and have a record of all the changes. 

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
![WhatsApp Image 2023-03-27 at 1 40 03 PM](https://user-images.githubusercontent.com/40188935/227904348-3516b301-f566-4d54-b68d-8f0029f0f099.jpeg)

#### Dockerized Program
- To create a Docker container, a Dockerfile is provided. Make sure Docker Desktop is installed. The Dockerfile contains the following 
```bash
FROM python:3.10-slim 
ADD . .
RUN pip install -r requirements.txt
EXPOSE 8500 
CMD ["python","checkssh.py"]
```

- To build the Docker image from the Dockerfile, run the following command: 
```bash
docker build -t checkip . 
```

- To run a Docker container with the name *checkipcontainer* on port 8500
```bash
docker run -p 8500:8500 --name checkipcontainer checkip
```