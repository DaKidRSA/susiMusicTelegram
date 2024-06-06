import sys
import os

# Append the parent directory of the current file to the system path
# This is done to ensure that the "config" module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import api_id, api_hash, bot_token
from handlers.bot import SusiClient

# Create an instance of the SusiClient class using the imported API ID, API hash, and bot token
# The SusiClient class is responsible for managing the bot's functionality
susi = SusiClient(api_id, api_hash, bot_token)