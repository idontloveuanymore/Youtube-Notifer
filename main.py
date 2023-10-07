from config import channel_ids, CHANNEL, access_token, file_name
from downloading import get_latest_video, wait
from posting import send_link_to_channel

# wait == time.sleep()

def moderation(video_link):
    print('mderation complete...') # u can delete this
    with open(file_name, mode='r') as file:
        lines = file.read().splitlines()
        if video_link in lines:
            return False
        return True

if __name__ == '__main__':
    while True:
        for channel_id in channel_ids:
            video_link, channel_name = get_latest_video(channel_id, access_token)
            moderation_result = moderation(video_link)
            if moderation_result:
                send_link_to_channel(CHANNEL, video_link, channel_name)
        wait(90)

# Restriction applies:
# 10,000 requests per day per project

# So calculate so that everything works properly!