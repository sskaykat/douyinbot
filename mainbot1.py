import re
import requests
import json
import telebot
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 从配置文件中获取Telegram Bot的API令牌
bot_token = config['Telegram']['BotToken']

# 创建Telegram Bot实例
bot = telebot.TeleBot(bot_token)

# 处理/start命令
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "欢迎使用视频URL获取机器人！请发送您的URL。")

# 处理用户发送的URL
@bot.message_handler(func=lambda message: True)
def handle_url(message):
    url_input = message.text
    urls = re.findall(r'https?://\S+', url_input)
    url = f"https://api.pearktrue.cn/api/video/api.php?url={urls}"

    response = requests.get(url)
    data = json.loads(response.text)

    if data["code"] == 200:
        video_url = data["data"]["url"]
        bot.send_video(message.chat.id, video_url)
    else:
        error_msg = data["msg"]
        bot.reply_to(message, f"请求失败: {error_msg}")

# 启动机器人
bot.polling()
