# Social Media Posting Script

This project provides a simple script to post messages to both Bluesky and Mastodon social media platforms using their respective APIs.

## Features

- Post messages to Bluesky.
- Post messages to Mastodon.
- Post messages to both platforms simultaneously.

## Prerequisites

- Python 3.x
- `atproto` library for Bluesky API
- `Mastodon.py` library for Mastodon API
- `python-dotenv` for loading environment variables

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/looprock/splitposter.git
   cd splitposter
   ```

2. Install the required packages:

This project is based on uv. You can create your virtual environment by navigating to the repo folder and running:

   ```
   uv sync
   ```

3. Create a `.env` file in the root directory and add your credentials:

   ```plaintext
   BLUESKY_USERNAME=your_bluesky_username
   BLUESKY_PASSWORD=your_bluesky_password
   MASTODON_ACCESS_TOKEN=your_mastodon_access_token
   MASTODON_API_BASE_URL=your_mastodon_api_base_url
   ```

## Usage

Run the script and enter your message when prompted:
