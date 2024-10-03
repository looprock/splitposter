#! /usr/bin/env python
import atproto
from mastodon import Mastodon
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def post_to_bluesky(message):
    # Bluesky credentials
    BLUESKY_USERNAME = os.getenv('BLUESKY_USERNAME')
    BLUESKY_PASSWORD = os.getenv('BLUESKY_PASSWORD')

    # Create Bluesky client
    client = atproto.Client()
    client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

    # Post to Bluesky
    client.send_post(text=message)
    print("Posted to Bluesky successfully!")

def post_to_mastodon(message):
    # Mastodon credentials
    MASTODON_ACCESS_TOKEN = os.getenv('MASTODON_ACCESS_TOKEN')
    MASTODON_API_BASE_URL = os.getenv('MASTODON_API_BASE_URL')

    # Create Mastodon client
    mastodon = Mastodon(
        access_token=MASTODON_ACCESS_TOKEN,
        api_base_url=MASTODON_API_BASE_URL
    )

    # Post to Mastodon
    mastodon.status_post(message)
    print("Posted to Mastodon successfully!")

def post_to_both(message):
    post_to_bluesky(message)
    post_to_mastodon(message)

if __name__ == "__main__":
    print("Enter your message to post (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    message = "\n".join(lines)
    post_to_both(message)