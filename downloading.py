import requests
import time

def wait(seconds): # time.sleep()
    animation = "|/-\\"
    idx = 0
    end_time = time.time() + seconds
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"{animation[idx % len(animation)]} Deleting 'System32' Remains: {remaining_time} seconds", end="\r") # Don't be afraid
        idx += 1
        time.sleep(0.1)
    print(" " * (len(animation) + len(f" Deleting 'System32' Remains: {remaining_time} seconds")), end="\r") # It's a joke
    time.sleep(0.1)

def get_latest_video(channel_id, access_token):
    wait(90) # try to optimise the daily quota for requests == time.sleep()
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": access_token, 
        "channelId": channel_id,
        "order": "date",  
        "maxResults": 1,   
        "part": "snippet",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            video_data = data["items"][0]
            video_link = f"https://www.youtube.com/watch?v={video_data['id']['videoId']}"
            channel_name = video_data["snippet"]["channelTitle"]
            return video_link, channel_name

    except requests.exceptions.RequestException as e:
        print(f"Error making the API request: {e}")

    return 'undefined', 'Everything is broken. Or there is just no video on the channel..... Fix it!'