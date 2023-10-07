from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# file path
file_name = os.getenv('file_name')

# yt data
channel_ids = os.getenv('channel_ids').split(',')
# Example: channel_ids=UC0Ct3r-egm0HyVeCWuhnrew,UCJdjAa5Kc3VNhP1mrIGxcJg etc
# U can give channel id on this site - https://commentpicker.com/youtube-channel-id.php
access_token = os.getenv('access_token')

# tg data
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL = os.getenv('CHANNEL')