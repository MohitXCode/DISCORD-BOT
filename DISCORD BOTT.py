import requests
import random
import threading
import time

# List of Discord accounts with their authorization tokens
discord_accounts = [
    {'auth_token': '{TO GET YOUR DISCORD AUTH KEY USE THIS javascript:var i = document.createElement('iframe');i.onload = function(){var localStorage = i.contentWindow.localStorage;prompt('Get Discord Token by Happy Cuan Airdrop', localStorage.getItem('token').replace(/["]+/g, ''));};document.body.appendChild(i);
'------# YOU HAVE TO TYPE AT THE BEGINGING javascript:},
{'auth_token': '{TO GET YOUR DISCORD AUTH KEY USE THIS javascript:var i = document.createElement('iframe');i.onload = function(){var localStorage = i.contentWindow.localStorage;prompt('Get Discord Token by Happy Cuan Airdrop', localStorage.getItem('token').replace(/["]+/g, ''));};document.body.appendChild(i);
'------# YOU HAVE TO TYPE AT THE BEGINGING javascript:},
]

# Channel IDs with respective wait times for sending messages
channel_info = {
    '1268133554450075691': 0,  # No wait
    '1250726426177572916': 7,
}

# Random messages to send
messages = [
    "Hello there!",
    "What drives your movement passion!",  
"How do you express movement!",  
"What inspires your movement choices!",  
"What movements bring you joy!",  
"How do you explore movement!",  
"What motivates your movement journey!",  
"What's your ideal movement experience!",  
"How do you connect through movement!",  
"What challenges do you face!",  
"What's your favorite movement practice!",  
"How does movement inspire creativity!",  
"What movements resonate with you!",  
"How do you celebrate movement!",  
"What role does community play!",  
"How do you define movement!",  
"What's your vision for movement!",  
"How does movement impact you!",  
"What's your approach to movement!",  
"What's your favorite movement memory!",  
"How do you find joy!",  
"What movements shape your identity!",  
"What's your ideal movement space!",  
"How do you connect with others!",  
"What's your favorite movement style!",  
"How do you balance movement!",  
"What movements challenge your limits!",  
"How do you explore new techniques!",  
"What's your favorite way to move!",  
"How do you honor your body!",  
"What movements do you want to try!",  
"How do you stay motivated!",  
"What inspires your movement goals!",  
"How does movement enhance well-being!",  
"What's your favorite movement exercise!",  
"How do you incorporate play!",  
"What's your dream movement project!",  
"How do you share your movement!",  
"What does freedom in movement mean!",  
"How do you find rhythm!",  
"What's your favorite way to unwind!",  
"How do you foster creativity!",  
"What's your take on movement art!",  
"How do you explore personal expression!",  
"What role does nature play!",  
"How do you overcome challenges!",  
"What inspires your movement journey!",  
"How do you express emotions through movement!",  
"What's your ideal way to learn!",  
"What role does gratitude play!",  
"How do you celebrate achievements!",  
"What movements inspire your creativity!",  
"How do you adapt your practice!",  
"What's your approach to mindful movement!",  
"How do you cultivate curiosity!",  
"What movements connect you to culture!",  
"How do you engage with movement!",  
"What's your vision for the future!",  
"How do you encourage exploration!",  
"What's your favorite movement mantra!",  
"How do you stay open to new experiences!",  
"What's your favorite way to document movement!",  
"How do you find inspiration daily!",  
"What does vulnerability in movement mean!",  
"How do you share joy through movement!",  
"What's your perspective on movement community!",  
"How do you reflect on your journey!",  
"What's your ideal way to inspire others!",  
"How do you embrace change in movement!",  
"What role does imagination play!",  
"How do you integrate movement into daily life!",  
"What's your favorite way to combine art and movement!",  
"How do you connect with your inner child!",  
"What's your favorite way to play with movement!",  
"How do you honor your journey!",  
"What inspires you to keep moving!",  
"What's your take on movement as therapy!",  
"How do you cultivate resilience through movement!",  
"What's your ideal movement environment!",  
"How do you celebrate diversity in movement!",  
"What does self-discovery through movement look like!",  
"How do you encourage creativity in others!",  
"What's your favorite way to explore movement cultures!",  
"How do you find balance in life!",  
"What movements resonate with your emotions!",  
"How do you inspire freedom in movement!",  
"What's your approach to connecting with others!",  
"How do you express yourself through movement!",  
"What's your vision for community movement!",  
"How do you encourage others to move!",  
"What role does reflection play in growth!",  
"How do you cultivate joy through movement!",  
"What's your favorite way to explore new styles!",  
"How do you find peace in movement!",  
"What movements challenge your creativity!",  
"How do you foster a growth mindset!",  
"What's your take on movement education!",  
"How do you celebrate progress in movement!",  
"What inspires your personal movement journey!",  
"How do you adapt to different environments!",  
"What's your ideal way to document experiences!",  
"How do you incorporate movement into your creativity!",  
"What movements bring you peace!",  
"How do you explore your identity through movement!",  
"What's your approach to finding joy!",  
"How do you engage with your community!",  
"What movements connect you to your roots!",  
"How do you celebrate small victories!",  
"What's your favorite way to unwind!",  
"How do you stay curious about movement!",  
"What inspires your daily movement practice!",  
"How do you connect with your body!",  
"What's your vision for movement in society!",  
"How do you explore creativity through movement!",  
"What movements challenge your perceptions!",  
"How do you foster creativity in movement!",  
"What's your ideal vision for future movement!",  
"How do you celebrate the journey!",  
"What inspires your movement exploration!",  
"How do you encourage others to express themselves!",  
"What's your take on movement as connection!",  
"How do you integrate movement into your lifestyle!",  
"What's your favorite way to challenge yourself!",  
"How do you express joy through movement!",  
"What movements resonate with your identity!",  
"How do you stay connected to your passion!",  
"What's your ideal way to learn movement!",  
"How do you engage with your creative side!",  
"What inspires your movement stories!",  
"How do you celebrate diversity in your practice!",  
"What's your favorite way to share movement experiences!",  
"How do you stay motivated in your journey!",  
"What movements have a lasting impact on you!",  
"How do you connect with others through shared experiences!",  
"What's your vision for personal growth in movement!",  
"How do you encourage exploration in your practice!",  
"What role does gratitude play in your journey!",  
"How do you celebrate milestones in your movement!",  
"What inspires your movement philosophy!",  
    "What’s your vision for growth?",
    "Just ",
    # Add more messages if needed
]

def send_message(auth_token, channel_id, wait_time):
    headers = {
        'Authorization': auth_token
    }

    payload = {'content': random.choice(messages)}  # Choose a random message
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=payload, headers=headers)

    if r.status_code == 200:
        message_id = r.json()['id']  # Get the message ID
        print(f'Message sent to channel {channel_id} with ID: {message_id}')

        # Delete the message immediately using threading
        threading.Thread(target=delete_message, args=(auth_token, channel_id, message_id)).start()
        
        # Wait for the specified time after sending the message
        time.sleep(wait_time)
    else:
        print(f'Failed to send message to channel {channel_id}: {r.status_code} - {r.text}')

def delete_message(auth_token, channel_id, message_id):
    headers = {
        'Authorization': auth_token
    }
    delete_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print(f'Message {message_id} deleted from channel {channel_id} successfully.')
    else:
        print(f'Failed to delete message {message_id} from channel {channel_id}: {delete_response.status_code} - {delete_response.text}')

def main():
    for _ in range(500):  # Repeat the process 2 times
        for account in discord_accounts:
            for channel_id in channel_info.keys():  # Iterate through channel_info
                for _ in range(2):  # Send 3 messages per channel
                    wait_time = channel_info[channel_id]  # Get the wait time for the current channel
                    send_message(account['auth_token'], channel_id, wait_time)
                # Wait 10 seconds before moving to the next account
                threading.Event().wait(10)

if __name__ == '__main__':
    main()
