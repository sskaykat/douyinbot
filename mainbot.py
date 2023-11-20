import requests
import telebot
import re
from config import TELEGRAM_BOT_TOKEN

# API解析URL
API_URL = 'https://api.tq23.cn/api/xd-jiexi?url='

# 初始化Telebot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 处理/start命令
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '欢迎使用视频解析Bot！发送视频链接以获取解析结果。')

# 处理用户发送的URL
@bot.message_handler(func=lambda message: True)
def handle_url(message):
    # 使用正则表达式提取消息中的URL
    url_match = re.search(r'(https?://[^\s]+)', message.text)
    
    if url_match:
        url = url_match.group(1)
        full_url = f'{API_URL}{url}'
        
        response = requests.get(full_url)

        if response.status_code == 200:
            data = response.json()
            video_url = data.get("video")
            if video_url:
                bot.send_video(message.chat.id, video_url)
            else:
                bot.reply_to(message, '解析失败，无法获取视频链接。')
        else:
            bot.reply_to(message, f'解析失败，错误码： {response.status_code}')
    else:
        bot.reply_to(message, '未找到有效的URL，请确保消息中包含有效的视频链接。')

# 启动Bot
bot.polling()
