import os
import telebot
from config import BOT_TOKEN, file_name

# Initialising the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Write the ID of the last video to a file
def write_videoid_to_file(file_name, video_link):
    with open(file_name, mode='a') as file:
        file.write(f'{video_link}\n')
    print('The link to the video has been writed!')

# Sending a link to a new video to your telegram channel
def send_link_to_channel(channel_id, link, channel_name):
    text = f'There is a new video on channel {channel_name}:\n{link}!'
    bot.send_message(chat_id=channel_id, text=text)
    print(f'The link was sent to channel {channel_id}!')
    write_videoid_to_file(file_name, link)